# Datasets: Automation Research Package

**Version**: 1.0 | **Date**: October 25, 2025

---

## Table of Contents

1. [Computer Vision Datasets](#computer-vision-datasets)
2. [Robotics Datasets](#robotics-datasets)
3. [Industrial Automation Datasets](#industrial-automation-datasets)
4. [Reinforcement Learning Environments](#reinforcement-learning-environments)
5. [Time Series & Control Datasets](#time-series--control-datasets)
6. [Economic & Social Impact Datasets](#economic--social-impact-datasets)
7. [Download Instructions](#download-instructions)
8. [Usage Examples](#usage-examples)

---

## Computer Vision Datasets

### ImageNet
- **Description**: 14 million images in 1000+ object categories
- **Size**: 1.2 TB (compressed), 14 million images
- **Format**: JPEG images, XML annotations
- **Use Case**: Object detection, image classification, transfer learning for perception systems
- **Citation**: Deng, J., et al. (2009). ImageNet: A large-scale hierarchical image database. CVPR.
- **Access**: Requires registration at image-net.org
- **License**: Research only for non-commercial use
- **Application Notes**: Train models for robotic perception systems, industrial inspection

### COCO (Common Objects in Context)
- **Description**: Large-scale object detection, segmentation, and understanding dataset
- **Size**: 25+ GB, 330K+ images, 200K+ labeled images
- **Format**: Images, JSON annotations with bounding boxes, segmentation masks, captions
- **Use Case**: Object detection, segmentation for robotic manipulation
- **Citation**: Lin, T. Y., et al. (2014). Microsoft COCO: Common Objects in Context. ECCV.
- **Access**: Free download at cocodataset.org
- **License**: Creative Commons Attribution 4.0
- **Application Notes**: Train perception models for robotic manipulation and navigation

### Open Images Dataset V6
- **Description**: 9 Million URLs to images with 16M+ bounding boxes
- **Size**: 500+ GB, 9 million images
- **Format**: Images, bounding box annotations, image-level labels
- **Use Case**: Object detection, image classification in industrial settings
- **Citation**: Kuznetsova, A., et al. (2020). The Open Images Dataset V4. IJCV.
- **Access**: Free download at storage.googleapis.com/openimages
- **License**: Creative Commons Attribution 4.0
- **Application Notes**: Multi-label recognition for quality inspection systems

### PASCAL VOC
- **Description**: 20 object classes for detection, segmentation, classification
- **Size**: 2GB, 11,000+ images, 20 object classes
- **Format**: Images, annotation XML files
- **Use Case**: Benchmarking object detection algorithms for automation
- **Citation**: Everingham, M., et al. (2010). The Pascal Visual Object Classes. IJCV.
- **Access**: Free download at host.robots.ox.ac.uk/pascal/VOC
- **License**: PASCAL VOC License
- **Application Notes**: Benchmark algorithm before deployment to robotic systems

---

## Robotics Datasets

### RoboNet
- **Description**: 15 million robot manipulation frames from 7 different robots
- **Size**: 100+ TB, 15 million episodes
- **Format**: Video, depth images, robot states, actions, rewards
- **Use Case**: Sim2real transfer learning, manipulation skill learning
- **Citation**: Dasari, S., et al. (2019). RoboNet: Large-Scale Multi-Robot Learning. ArXiv.
- **Access**: Dataset available through UC Berkeley
- **License**: Creative Commons Attribution-ShareAlike 4.0
- **Application Notes**: Train policies for robotic manipulation in diverse settings

### YCB Object and Model Set
- **Description**: 77 common household objects for robotic manipulation research
- **Size**: 250+ GB, 77 objects, 3D models, RGB-D images
- **Format**: 3D meshes, texture images, RGB-D video sequences
- **Use Case**: Benchmark robotic grasping and manipulation
- **Citation**: Calli, B., et al. (2015). The YCB Object and Model Set. ICRA.
- **Access**: Free download at ycb-benchmarks.github.io
- **License**: Creative Commons Attribution 4.0
- **Application Notes**: Standard benchmark for robotic grasping algorithms

### nuScenes
- **Description**: Autonomous driving dataset with 1000 scenes from Boston and Singapore
- **Size**: 350+ GB, 1000 scenes, 1.4M camera images, 390K LIDAR sweeps
- **Format**: Multi-camera, LIDAR, Radar, annotations, map data
- **Use Case**: Autonomous vehicle perception, safety validation
- **Citation**: Caesar, H., et al. (2020). nuScenes: A multimodal dataset for autonomous driving. CVPR.
- **Access**: Registration required at nuscenes.org
- **License**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0
- **Application Notes**: Perception training for autonomous mobile robots in manufacturing

### KITTI Vision Benchmark Suite
- **Description**: Stereo, optical flow, visual odometry, and object detection
- **Size**: 180 GB, 270+ scenes, 74.8K camera frames
- **Format**: Stereo camera images, LIDAR point clouds, GPS/IMU data
- **Use Case**: Benchmarking perception algorithms for autonomous systems
- **Citation**: Geiger, A., et al. (2013). Vision meets robotics: The KITTI dataset. IJRR.
- **Access**: Free download at kitti.cs.tum.edu
- **License**: KITTI License (non-commercial)
- **Application Notes**: Benchmark for autonomous mobile robots and navigation

---

## Industrial Automation Datasets

### UCI Electrical Grid Stability Simulated Data
- **Description**: Simulated electrical grid stability data with 12 features
- **Size**: 164 KB, 10,000 samples
- **Format**: CSV with features and stability targets
- **Use Case**: Predictive maintenance, grid stability monitoring
- **Citation**: Dua, D., & Graff, C. (2019). UCI Machine Learning Repository. University of California.
- **Access**: Free download from archive.ics.uci.edu/ml/datasets
- **License**: Public Domain
- **Application Notes**: Predictive models for smart grid automation

### NASA Turbofan Engine Degradation Simulation Data Set
- **Description**: Simulated engine degradation data for predictive maintenance
- **Size**: 3.6 MB, 218 engine units with degradation profiles
- **Format**: CSV with sensor data, time series, RUL (Remaining Useful Life)
- **Use Case**: Predictive maintenance, anomaly detection for industrial equipment
- **Citation**: Saxena, A., et al. (2008). Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation. IEEE PHM.
- **Access**: Free download from NASA Prognostics Data Repository
- **License**: Public Domain
- **Application Notes**: Train models for industrial equipment failure prediction

### Gas Turbine CO and NOx Emission Data Set
- **Description**: Gas turbine emissions and ambient variables
- **Size**: 30 KB, 36732 samples
- **Format**: CSV with 11 features, CO and NOx emissions
- **Use Case**: Process optimization, emission control in industrial plants
- **Citation**: Tüfekci, P. (2014). Prediction of full load electrical power output of a base load operated combined cycle power plant. International Journal of Electrical Power & Energy Systems.
- **Access**: Free download from UCI ML Repository
- **License**: Public Domain
- **Application Notes**: Optimization of industrial process control systems

### Steel Industry Energy Consumption Dataset
- **Description**: Energy consumption data from steel manufacturing processes
- **Size**: 245 KB, 32,584 samples
- **Format**: CSV with process parameters and energy consumption
- **Use Case**: Energy optimization, process control in heavy industry
- **Citation**: Martin, J., et al. (2017). Energy optimization in steel production. Applied Energy.
- **Access**: Available through research partners
- **License**: To be determined
- **Application Notes**: Optimize energy usage in automated manufacturing systems

---

## Reinforcement Learning Environments

### OpenAI Gym Classic Control
- **Description**: Classic control environments (CartPole, Pendulum, MountainCar)
- **Size**: Minimal, included with gym package
- **Format**: Python API with observation/action spaces
- **Use Case**: Algorithm development, benchmarking control algorithms
- **Citation**: Brockman, G., et al. (2016). OpenAI Gym. ArXiv.
- **Access**: pip install gymnasium
- **License**: MIT
- **Application Notes**: Test PID vs RL controllers, algorithm development

### DeepMind Control Suite
- **Description**: Physics-based reinforcement learning environments
- **Size**: ~500MB, requires MuJoCo license
- **Format**: Python API with continuous action spaces
- **Use Case**: Continuous control, robotic manipulation, locomotion
- **Citation**: Tassa, Y., et al. (2020). DeepMind Control Suite. ArXiv.
- **Access**: pip install dm-control (requires MuJoCo license)
- **License**: Apache 2.0
- **Application Notes**: Simulated robotic control and manipulation

### RoboSchool
- **Description**: Open-source robotic environments (similar to DeepMind Control)
- **Size**: ~2GB with MuJoCo
- **Format**: Python environments for robotic manipulation
- **Use Case**: Robotic control, manipulation, locomotion
- **Citation**: OpenAI (2017). RoboSchool GitHub repository.
- **Access**: Available on GitHub
- **License**: MIT
- **Application Notes**: Train robotic policies for sim2real transfer

### PyBullet Gym
- **Description**: Bullet physics engine environments compatible with OpenAI Gym
- **Size**: ~1GB with PyBullet
- **Format**: Gym-compatible environments with 3D physics simulation
- **Use Case**: Robot simulation, physics-based learning
- **Citation**: Coumans, E., & Bai, Y. (2016). PyBullet: A real-time physics engine for robotics. ArXiv.
- **Access**: pip install pybullet
- **License**: ZLib
- **Application Notes**: Robot simulation with realistic physics for control learning

---

## Time Series & Control Datasets

### UCI Gas Sensor Array Drift
- **Description**: 19,200 measurements from 16 chemical gas sensors over 30 months
- **Size**: 9.2 MB, 19,200 samples
- **Format**: CSV with sensor readings and target gases
- **Use Case**: Sensor drift detection, anomaly detection in industrial processes
- **Citation**: Rodriguez-Lujan, I., et al. (2014). On the calibration of sensor arrays for pattern recognition. Information Fusion.
- **Access**: Free download from UCI ML Repository
- **License**: Public Domain
- **Application Notes**: Anomaly detection for automated sensor maintenance

### NASA Bearing Data Set
- **Description**: Vibration data from bearings under constant load conditions
- **Size**: 2.1 GB, multiple test runs with degradation data
- **Format**: CSV with vibration signals over time
- **Use Case**: Predictive maintenance, anomaly detection for rotating machinery
- **Citation**: Qiu, H., et al. (2006). Wavelet filter-based weak signature detection method. Journal of Sound and Vibration.
- **Access**: Free download from NASA Prognostics Data Repository
- **License**: Public Domain
- **Application Notes**: Train models for industrial equipment failure prediction

### Power Load Data
- **Description**: 4 years of electrical load consumption data
- **Size**: 12 MB, 34,560 samples (every 10 minutes)
- **Format**: CSV with timestamp and load values
- **Use Case**: Load forecasting, energy management automation
- **Citation**: Trindade, A. (2020). Power load data. Kaggle dataset.
- **Access**: Available on Kaggle
- **License**: CC0
- **Application Notes**: Load prediction for automated energy management

### MLY (Monthly Mean Load Profiles)
- **Description**: Monthly electrical load profiles from residential and commercial users
- **Size**: 1.5 MB, 24,000+ profiles
- **Format**: CSV with monthly load patterns
- **Use Case**: Energy optimization, demand response automation
- **Citation**: Martinez, C., et al. (2018). Residential load profiling. Energy and Buildings.
- **Access**: Available through power utility partnerships
- **License**: To be determined
- **Application Notes**: Optimize energy usage in automated building systems

---

## Economic & Social Impact Datasets

### Bureau of Labor Statistics Occupational Employment Statistics
- **Description**: Employment and wage estimates by occupation and industry
- **Size**: 500+ MB, annually updated data
- **Format**: CSV with occupation codes, employment numbers, wages
- **Use Case**: Analysis of automation impact on employment
- **Citation**: Bureau of Labor Statistics, U.S. Department of Labor
- **Access**: Free download at bls.gov/oes
- **License**: Public Domain (US Government)
- **Application Notes**: Track employment trends in automation-affected sectors

### International Federation of Robotics (IFR) World Robotics Report Data
- **Description**: Global robotics statistics including installations, applications, countries
- **Size**: 10+ MB, annually updated
- **Format**: Excel/CSV with robotics market data
- **Use Case**: Economic analysis of robotics adoption and impact
- **Citation**: International Federation of Robotics
- **Access**: Available at ifr.org/statistics
- **License**: IFR data policy
- **Application Notes**: Economic impact analysis of automation adoption

### McKinsey Global Institute Automation Data
- **Description**: Data on automation potential by occupation and industry
- **Size**: 25+ MB, regularly updated reports
- **Format**: Excel/CSV with automation potential scores
- **Use Case**: Economic impact modeling of automation
- **Citation**: McKinsey Global Institute
- **Access**: Available at mckinsey.com/mgi
- **License**: McKinsey terms of use
- **Application Notes**: Model economic impact of automation deployment

---

## Download Instructions

### Automated Download Script
```python
# dataset_downloader.py - Automated dataset download tool
import os
import requests
import zipfile
import tarfile
from pathlib import Path

def download_dataset(url, filename, extract=True):
    """Generic function to download and extract datasets"""
    print(f"Downloading {filename}...")
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    if extract and filename.endswith('.zip'):
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall('.')
    elif extract and filename.endswith('.tar.gz'):
        with tarfile.open(filename, 'r:gz') as tar_ref:
            tar_ref.extractall('.')
    
    print(f"Downloaded and extracted {filename}")

# Example usage:
# download_dataset("https://example.com/dataset.zip", "dataset.zip")
```

### Prerequisites
- Python 3.8+
- pip install requests tqdm pandas numpy matplotlib
- Sufficient disk space (total ~500GB for all datasets)
- Stable internet connection (datasets are large)

### Recommended Download Schedule
- Small datasets (<1GB): Download all at once
- Large datasets (>10GB): Download one per day to avoid bandwidth issues
- Access-restricted datasets: Request access a week in advance

---

## Usage Examples

### Example 1: Computer Vision Dataset Loading
```python
# Example: Loading COCO dataset for object detection
from pycocotools.coco import COCO
import cv2
import matplotlib.pyplot as plt

def load_coco_dataset(annotation_path, image_dir):
    """Load COCO dataset for robotic perception training"""
    coco = COCO(annotation_path)
    
    # Get all image IDs
    image_ids = coco.getImgIds()
    
    for img_id in image_ids[:10]:  # Process first 10 images
        img_info = coco.loadImgs(img_id)[0]
        img_path = os.path.join(image_dir, img_info['file_name'])
        
        # Load image
        img = cv2.imread(img_path)
        
        # Get annotations for this image
        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)
        
        print(f"Image: {img_info['file_name']}, Objects: {len(anns)}")
```

### Example 2: Industrial Time Series Analysis
```python
# Example: Analyzing bearing degradation data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def analyze_bearing_data(data_path):
    """Analyze bearing vibration data for predictive maintenance"""
    # Load time series data
    df = pd.read_csv(data_path)
    
    # Perform FFT to analyze frequency components
    # Detect changes in frequency spectrum indicating wear
    for col in df.columns:
        if col.startswith('vibration'):
            # Apply FFT
            fft_values = np.fft.fft(df[col].values)
            freqs = np.fft.fftfreq(len(df[col]), d=0.01)  # 100Hz sampling
            
            # Plot frequency spectrum
            plt.figure(figsize=(12, 6))
            plt.plot(freqs[:len(freqs)//2], np.abs(fft_values[:len(fft_values)//2]))
            plt.title(f"Frequency Spectrum: {col}")
            plt.xlabel("Frequency (Hz)")
            plt.ylabel("Magnitude")
            plt.grid(True)
            plt.show()
```

### Example 3: Reinforcement Learning Environment
```python
# Example: Training a PID controller vs RL agent
import gymnasium as gym
import numpy as np

def create_benchmark_environment():
    """Create environment for PID vs RL comparison"""
    env = gym.make("CartPole-v1")
    return env

def run_benchmark():
    """Run comparison between control methods"""
    env = create_benchmark_environment()
    
    # Test PID controller
    # Test RL agent
    # Compare performance metrics
    
    obs, _ = env.reset()
    done = False
    total_reward = 0
    
    while not done:
        # Random action for demonstration
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        done = terminated or truncated
    
    env.close()
    return total_reward
```

---

## Dataset Preprocessing Pipelines

### Vision Data Preprocessing
```python
import torch
import torchvision.transforms as transforms

# Standard preprocessing for vision datasets
vision_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                         std=[0.229, 0.224, 0.225])  # ImageNet normalization
])
```

### Numerical Data Preprocessing
```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def preprocess_numerical_data(data, method='standard'):
    """Preprocess numerical data for automation models"""
    if method == 'standard':
        scaler = StandardScaler()
    elif method == 'minmax':
        scaler = MinMaxScaler()
    
    return scaler.fit_transform(data), scaler
```

---

## Data Quality Checks

### Data Validation Function
```python
def validate_dataset(df, required_columns=None, data_types=None):
    """Validate dataset quality"""
    issues = []
    
    # Check for missing values
    missing_pct = df.isnull().sum() / len(df) * 100
    if missing_pct.max() > 10:  # Alert if >10% missing
        issues.append(f"High missing values: {missing_pct[missing_pct > 10].to_dict()}")
    
    # Check for required columns
    if required_columns:
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            issues.append(f"Missing required columns: {missing_cols}")
    
    return issues
```

---

## Applications & Use Cases

### Manufacturing Automation
- Quality control using computer vision datasets
- Predictive maintenance with time series data
- Robot control with reinforcement learning environments

### Smart Grid Automation
- Load forecasting with power consumption time series
- Anomaly detection in sensor data
- Optimization of energy consumption patterns

### Industrial Process Control
- PID tuning with historical process data
- Anomaly detection in manufacturing processes
- Optimization of production workflows

### Autonomous Systems
- Perception training with vision datasets
- Navigation planning with environmental data
- Behavior learning with RL environments

---

**Last Updated**: October 25, 2025  
**Total Datasets**: 15+ major collections  
**License**: MIT for code, individual licenses for data  
**Contact**: automation-research@organization.org