# File: experiments/perception_actuation/main.py
import torch
import torchvision.transforms as transforms
from torchvision.models import mobilenet_v2
from PIL import Image
import time
import numpy as np

class PerceptionActuationPipeline:
    def __init__(self):
        self.model = mobilenet_v2(pretrained=True)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485,0.456,0.406], [0.229,0.224,0.225])
        ])
        with open("imagenet_classes.txt") as f:
            self.labels = [line.strip() for line in f.readlines()]
    
    def perceive(self, image_path):
        img = Image.open(image_path).convert("RGB")
        input_tensor = self.transform(img).unsqueeze(0)
        with torch.no_grad():
            output = self.model(input_tensor)
        _, pred_idx = torch.max(output, 1)
        return self.labels[pred_idx.item()], pred_idx.item()
    
    def actuate(self, class_name):
        print(f"Actuation: Detected {class_name} \u2192 Action: Approach/Grasp")
        time.sleep(0.1)  # Simulate actuation delay

# Run experiment
pipeline = PerceptionActuationPipeline()
latencies = []
for i in range(10):
    start = time.time()
    label, idx = pipeline.perceive("test_image.jpg")
    pipeline.actuate(label)
    latency = time.time() - start
    latencies.append(latency)
    print(f"Trial {i+1}: {label}, Latency: {latency:.3f}s")

print(f"\nMean Latency: {np.mean(latencies):.3f}s, Std: {np.std(latencies):.3f}s")