# Perception-to-Actuation Pipeline Experiment

This experiment demonstrates a complete perception-to-actuation pipeline using a pre-trained MobileNetV2 model for object classification and simulated actuation response.

## Description

The `main.py` script implements a `PerceptionActuationPipeline` class that uses a pre-trained MobileNetV2 model to classify objects in an input image. The system then simulates an actuation response based on the detected object class. The experiment measures the latency between perception and actuation over 10 trials.

## Installation

To run this experiment, you need to install the dependencies listed in the main `requirements.txt` file.

```bash
pip install -r ../../../requirements.txt
```

## Running the Experiment

To run the experiment, execute the `main.py` script from within this directory:

```bash
python main.py
```

## Expected Results

The script will load the MobileNetV2 model, classify the `test_image.jpg` file, and simulate actuation responses. It will output the classification results and latency measurements for 10 trials, followed by mean and standard deviation of the latencies.

## Required Files

This experiment requires:
- `imagenet_classes.txt`: Text file containing the 1000 ImageNet class labels
- `test_image.jpg`: Input image for classification

## Troubleshooting

If you encounter any issues, please ensure that all required files are present in the directory and that all required packages are installed correctly.