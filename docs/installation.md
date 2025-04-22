# Installation Guide

This guide provides step-by-step instructions for setting up the Smart Farming project on your local machine.

## Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package manager)
- Recommended: 8GB+ RAM for model training

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-farming.git
cd smart-farming
```

## 2. Set Up Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes all necessary packages:

```
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0
matplotlib>=3.4.0
seaborn>=0.11.0
streamlit>=1.10.0
torch>=1.10.0
torchvision>=0.11.0
pillow>=8.3.0
joblib>=1.0.0
opencv-python>=4.5.0
```

## 4. Download Datasets

### Crop Recommendation Datasets

1. Download the basic dataset from [Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) and save it as `data/raw/Crop_recommendation.csv`

2. Download the extended dataset from [Mendeley Data](https://data.mendeley.com/datasets/8v757rr4st/1/files/98242fd3-1912-4a59-ab26-23d97b454218) and save it as `data/raw/Crop Recommendation using Soil Properties and Weather Prediction.csv`

### Field Image Dataset

Download the Agriculture-Vision Mini-Scale dataset:

```bash
# Create a download directory
mkdir -p downloads

# Download the dataset
wget -O downloads/data2017_miniscale.tar.gz https://agriculture-vision.intelinair.com/Dataset/data2017_miniscale.tar.gz

# Extract the dataset
tar -xzf downloads/data2017_miniscale.tar.gz
```

Alternatively, download the dataset manually from [Agriculture-Vision Dataset](https://agriculture-vision.intelinair.com/Dataset/data2017_miniscale.tar.gz) and extract it to the project root.

## 5. Create Required Directories

```bash
# Create directories for data
mkdir -p data/raw
mkdir -p data/processed
mkdir -p data/processed/field_dataset

# Create directories for models and results
mkdir -p models/field_classifier
mkdir -p results/visualizations
mkdir -p results/reports
```

## 6. Preprocess the Data

```bash
# Process crop recommendation data
python src/preprocessing/preprocess_data.py

# Process field images
python src/preprocessing/process_field_dataset.py --data_dir data2017_miniscale --output_dir data/processed/field_dataset
```

## 7. Train Models

```bash
# Train basic crop recommendation model
python src/training/crop_prediction_model.py

# Train combined models
python src/training/train_combined_model.py

# Train field classifier (takes longer)
python src/training/field_classifier.py --dataset_dir data/processed/field_dataset --model_type resnet --epochs 3
```

Note: Model training may take significant time depending on your hardware. The field classifier requires a GPU for efficient training. If a GPU is not available, increase `--epochs` to achieve better results with longer training time.

## 8. Verify Installation

To verify that everything is installed correctly, run:

```bash
python run_all_apps.py
```

This should launch all three Streamlit web applications in your default browser.

## Troubleshooting

### "No module named..." errors

If you see errors about missing modules, ensure your virtual environment is activated and try reinstalling dependencies:

```bash
pip install -r requirements.txt --force-reinstall
```

### CUDA errors with PyTorch

If you encounter CUDA-related errors, install the appropriate PyTorch version for your system:

```bash
# For CUDA 11.7
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 --extra-index-url https://download.pytorch.org/whl/cu117

# For CPU only
pip install torch==1.13.1+cpu torchvision==0.14.1+cpu --extra-index-url https://download.pytorch.org/whl/cpu
```

### Out of Memory Errors

If you encounter memory issues during model training:
- Reduce batch size in the training scripts
- Close other memory-intensive applications
- Use a machine with more RAM/VRAM

### Port already in use errors

If Streamlit shows "Port already in use" errors:
- Stop any running Streamlit applications
- Change the port in the `run_all_apps.py` script
- Restart your computer if the issue persists 