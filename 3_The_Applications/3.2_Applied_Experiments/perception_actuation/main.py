# main.py - Perception to Actuation Pipeline Experiment

import torch
import torchvision.models as models
import torchvision.transforms as transforms
import numpy as np
import time

# 1. Load a pre-trained MobileNetV2 model
# The model is loaded in evaluation mode
model = models.detection.fasterrcnn_mobilenet_v3_large_320_fpn(pretrained=True)
model.eval()

# COCO class names
COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

def detect_objects(model, image):
    """Performs object detection on an image."""
    with torch.no_grad():
        prediction = model([image])
    
    labels = [COCO_INSTANCE_CATEGORY_NAMES[i] for i in prediction[0]['labels']]
    return labels

def map_action(objects):
    """Maps detected objects to simulated actions."""
    if 'person' in objects:
        print("Action: Human detected, slowing down.")
    elif 'car' in objects:
        print("Action: Car detected, maintaining distance.")
    elif 'stop sign' in objects:
        print("Action: Stop sign detected, initiating stop.")
    else:
        print("Action: No critical objects detected, proceeding.")

def main():
    """Main function to run the experiment."""
    # Create a dummy image (3 channels, 320x320)
    # In a real application, you would load and preprocess an image here
    transform = transforms.Compose([transforms.ToTensor()])
    dummy_image = torch.rand(3, 320, 320)

    print("Running perception-to-actuation pipeline...")

    # Run the pipeline 10 times to get an average latency
    latencies = []
    for _ in range(10):
        start_time = time.time()

        # 1. Perception: Detect objects in the image
        detected_objects = detect_objects(model, dummy_image)

        # 2. Action: Map detected objects to actions
        map_action(detected_objects)

        end_time = time.time()
        latency = (end_time - start_time) * 1000  # Convert to milliseconds
        latencies.append(latency)

    avg_latency = np.mean(latencies)
    print(f"\nAverage latency over 10 runs: {avg_latency:.2f} ms")

if __name__ == "__main__":
    main()
