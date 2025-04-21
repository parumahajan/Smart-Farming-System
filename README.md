# Smart Farming - Crop Recommendation and Field Analysis

A comprehensive smart farming system that combines soil analysis, weather data, and field imagery to provide crop recommendations and identify field conditions.

## Overview

This project includes three major components:
1. **Crop Recommendation System** - Recommends optimal crops based on soil properties and climate data
2. **Advanced Crop Recommendation System** - Uses extended dataset with seasonal weather predictions
3. **Field Condition Analyzer** - Identifies field conditions using computer vision

## Datasets

### Crop Recommendation Datasets
1. **Basic Crop Recommendation Dataset** - Contains N, P, K values, temperature, humidity, pH, rainfall, and suitable crops
   - Source: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
   - 2200+ samples with 7 input features and 22 crop classes

2. **Extended Crop Recommendation Dataset** - Includes seasonal weather predictions and more detailed soil analysis
   - Source: [Mendeley Data](https://data.mendeley.com/datasets/8v757rr4st/1/files/98242fd3-1912-4a59-ab26-23d97b454218)
   - 3800+ samples with 29 input features

### Field Image Dataset
- **Source**: [Agriculture-Vision Dataset (Mini-Scale)](https://agriculture-vision.intelinair.com/Dataset/data2017_miniscale.tar.gz)
- **Content**: 7,000+ high-resolution aerial field images with corresponding labels and segmentation masks
- **Structure**:
  - `field_images/`: RGB aerial photographs of agricultural fields
  - `field_labels/`: Categorical annotations for 9 field conditions
  - `field_masks/`: Pixel-level segmentation masks for condition areas
  - `field_bounds/`: Field boundary information
  - `field_stats.json`: Dataset statistics and metadata
- **Field Conditions**: Includes annotations for double plant, drydown, endrow, nutrient deficiency, planter skip, storm damage, water, waterway, and weed clusters
- **Processing**: Images resized to 224×224 pixels and normalized for model training
- **Augmentation**: Random flips, rotations, and color adjustments to improve model robustness
- **Split**: 70% training, 15% validation, 15% testing while preserving class distribution

## Models

1. **Basic Random Forest Model** - For crop recommendation based on basic soil and climate data
   - Accuracy: ~90%
   
2. **Combined Random Forest Model** - Trained on combined datasets
   - Accuracy: ~67%
   
3. **Extended Random Forest Model** - Uses all available features from the extended dataset
   - Accuracy: ~52%
   
4. **ResNet Field Classifier** - Identifies field conditions from aerial imagery
   - Trained for 3 epochs with ~75% accuracy

## Project Structure

```
smart-farming/
├── data/
│   ├── raw/                    # Raw datasets
│   └── processed/              # Processed datasets
├── models/                     # Trained models
│   ├── field_classifier/       # Field image classifier models
│   ├── random_forest_model.pkl
│   ├── random_forest_combined.pkl
│   └── random_forest_extended.pkl
├── results/                    # Model evaluation results
│   ├── visualizations/         # Charts and plots
│   └── reports/                # Performance reports
├── src/
│   ├── preprocessing/          # Data preprocessing scripts
│   ├── training/               # Model training scripts
│   ├── utils/                  # Utility functions
│   └── webapp/                 # Streamlit applications
└── docs/                       # Documentation
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-farming.git
cd smart-farming

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

Run all three apps simultaneously:
```bash
python run_all_apps.py
```

Or run individual apps:
```bash
# Field Analyzer
streamlit run src/webapp/app.py

# Basic Crop Recommender
streamlit run src/webapp/crop_recommendation_app.py

# Advanced Crop Recommender
streamlit run src/webapp/combined_model_app.py
```

## Team Members

- [Your Name] - Data Preprocessing and Integration
- [Team Member 2] - Model Training and Evaluation
- [Team Member 3] - Web Application Development
- [Team Member 4] - Computer Vision Implementation

## License

This project is licensed under the MIT License - see the LICENSE file for details. 

## File Locations

### Processed Datasets
- **Basic Crop Recommendation**: `data/processed/feature_stats.csv`
- **Extended Crop Recommendation**: `data/processed/extended_preprocessed.csv`
- **Combined Dataset**: `data/processed/feature_stats_combined.csv`
- **Processed Field Images**: `data/processed/field_dataset/`
  - Training images: `data/processed/field_dataset/train/`
  - Validation images: `data/processed/field_dataset/val/`
  - Test images: `data/processed/field_dataset/test/`

### Trained Models
- **Basic Crop Recommender**: `models/random_forest_model.pkl`
- **Combined Crop Recommender**: `models/random_forest_combined.pkl`
- **Extended Crop Recommender**: `models/random_forest_extended.pkl`
- **Field Analyzer**: `models/field_classifier/resnet_20250419_044617/best_model.pth`
- **Label Encoders**:
  - Basic model: `models/label_encoder.pkl`
  - Combined model: `models/combined_label_encoder.pkl`

### Evaluation Results
- **Model Reports**: `results/reports/`
  - Basic model: `results/classification_report.txt`, `results/model_accuracy.txt`
  - Combined model: `results/combined_classification_report.txt`, `results/combined_model_accuracy.txt`
  - Extended model: `results/extended_classification_report.txt`, `results/extended_model_accuracy.txt`
- **Visualizations**: `results/visualizations/`
  - Feature importance: `results/visualizations/feature_importance.png`
  - Confusion matrices: `results/visualizations/confusion_matrix.png`

### Web Applications
- **Field Analyzer**: `src/webapp/app.py`
- **Basic Crop Recommender**: `src/webapp/crop_recommendation_app.py`
- **Combined Crop Recommender**: `src/webapp/combined_model_app.py`
- **Multi-app Launcher**: `run_all_apps.py`

## Dataset Access

Due to GitHub file size limitations, the actual datasets are not included in this repository. Instead, they are available via the following links:

### Crop Recommendation Datasets
- **Processed Data ZIP File**: [Google Drive Link](https://drive.google.com/drive/folders/1FP1-v5HCPQm-zi4kzRFppWJkYj7HBa3s?usp=drive_link)
  - Contains all preprocessed CSV files and required PKL files
  - Extract to the project root directory to maintain the correct file structure

### Field Image Dataset
- **Field Dataset ZIP File**: [Google Drive Link](https://drive.google.com/drive/folders/1FP1-v5HCPQm-zi4kzRFppWJkYj7HBa3s?usp=drive_link)
  - Contains all processed field images with corresponding labels and masks
  - Extract to `data/processed/` directory

### Original Data Sources
If you prefer to download and process the raw datasets yourself:
1. **Basic Crop Recommendation Dataset**: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
2. **Extended Crop Recommendation Dataset**: [Mendeley Data](https://data.mendeley.com/datasets/8v757rr4st/1/files/98242fd3-1912-4a59-ab26-23d97b454218)
3. **Field Image Dataset**: [Agriculture-Vision Dataset (Mini-Scale)](https://agriculture-vision.intelinair.com/Dataset/data2017_miniscale.tar.gz)

After downloading, follow the preprocessing instructions in `docs/data_preprocessing.md` to prepare the data for use with the models. 