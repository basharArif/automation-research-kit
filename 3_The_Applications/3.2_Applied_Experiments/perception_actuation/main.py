# File: experiments/perception_actuation/main.py
#
# Experiment: Perception-to-Actuation Latency Measurement
# NOTE: Actuation is *simulated* (time.sleep). This experiment measures perception
# inference latency + the overhead of the actuation interface call.
# To extend to real actuation: replace actuate() with serial/ROS command.

import torch
import torchvision.transforms as transforms
from torchvision.models import MobileNet_V2_Weights, mobilenet_v2
from PIL import Image
import time
import numpy as np

class PerceptionActuationPipeline:
    def __init__(self):
        # Use the new weights API (torchvision >= 0.13); pretrained=True is deprecated
        weights = MobileNet_V2_Weights.DEFAULT
        self.model = mobilenet_v2(weights=weights)
        self.model.eval()
        # Use the preprocessing transforms recommended by the weight set
        self.transform = weights.transforms()
        self.labels = weights.meta["categories"]

    def perceive(self, image_path):
        """Run inference; return (class_name, class_index, inference_latency_ms)."""
        img = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(img).unsqueeze(0)
        t0 = time.perf_counter()
        with torch.no_grad():
            output = self.model(input_tensor)
        inference_ms = (time.perf_counter() - t0) * 1000
        _, pred_idx = torch.max(output, 1)
        return self.labels[pred_idx.item()], pred_idx.item(), inference_ms

    def actuate(self, class_name):
        """Simulated actuation: prints command and sleeps to model actuator response delay.
        Replace with serial command (pyserial) or ROS2 topic publish for real hardware."""
        print(f"  [CMD] Approach/Grasp → target class: {class_name}")
        time.sleep(0.05)  # Simulated 50ms actuator response delay

# ── Main experiment ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    pipeline = PerceptionActuationPipeline()
    inference_latencies_ms = []
    total_latencies_ms = []

    print(f"{'Trial':>5} | {'Class':35} | {'Inference(ms)':>13} | {'Total(ms)':>9}")
    print("-" * 70)

    for i in range(10):
        t_start = time.perf_counter()
        label, idx, inf_ms = pipeline.perceive("test_image.jpg")
        pipeline.actuate(label)
        total_ms = (time.perf_counter() - t_start) * 1000

        inference_latencies_ms.append(inf_ms)
        total_latencies_ms.append(total_ms)
        print(f"{i+1:>5} | {label:35} | {inf_ms:>13.1f} | {total_ms:>9.1f}")

    print("\n── Results ──────────────────────────────────────────────────────────")
    print(f"Inference latency : mean={np.mean(inference_latencies_ms):.1f}ms  "
          f"p95={np.percentile(inference_latencies_ms, 95):.1f}ms")
    print(f"Total latency     : mean={np.mean(total_latencies_ms):.1f}ms  "
          f"p95={np.percentile(total_latencies_ms, 95):.1f}ms")
    print(f"Target: inference < 50ms for real-time robotics (MobileNetV2 on CPU should achieve this)")