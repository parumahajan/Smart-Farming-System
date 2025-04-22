# Data Preprocessing

This document outlines the data preprocessing steps performed for the Smart Farming project. The preprocessing pipeline transforms raw agricultural data into structured formats suitable for machine learning models.

## Datasets

Our project utilizes three main data sources:

### 1. Basic Crop Recommendation Dataset
- **Source**: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- **File**: `data/raw/Crop_recommendation.csv`
- **Description**: Contains soil nutrient levels (N, P, K), climate data, and suitable crops
- **Size**: 2,200+ samples, 8 columns
- **Format**: CSV

### 2. Extended Crop Recommendation Dataset
- **Source**: [Mendeley Data](https://data.mendeley.com/datasets/8v757rr4st/1/files/98242fd3-1912-4a59-ab26-23d97b454218)
- **File**: `data/raw/Crop Recommendation using Soil Properties and Weather Prediction.csv`
- **Description**: Contains detailed soil properties and seasonal weather predictions
- **Size**: 3,800+ samples, 29 columns
- **Format**: CSV

### 3. Field Image Dataset
- **Source**: [Agriculture-Vision Dataset (Mini-Scale)](https://agriculture-vision.intelinair.com/Dataset/data2017_miniscale.tar.gz)
- **Directory**: `data2017_miniscale/`
- **Description**: Aerial field imagery with labels and masks
- **Contents**:
  - `field_images/`: RGB aerial images
  - `field_labels/`: Classification labels
  - `field_masks/`: Segmentation masks
  - `field_bounds/`: Field boundary information
  - `field_stats.json`: Dataset statistics

## Preprocessing Pipeline

### 1. Crop Recommendation Data

#### Basic Dataset Preprocessing
```python
# Implementation in src/preprocessing/preprocess_crop_data.py
```

1. **Data Loading and Inspection**
   - Load CSV file
   - Check for missing values
   - Analyze feature distributions
   - Examine class distribution

2. **Feature Engineering**
   - Feature scaling using StandardScaler
   - No dimensionality reduction needed due to the small number of features

3. **Data Splitting**
   - 80% training, 20% testing
   - Stratified split to maintain class distribution

4. **Label Encoding**
   - Transform crop names to numeric labels
   - Save label encoder for inference

5. **Data Storage**
   - Save processed data to `data/processed/crop_recommendation_data.csv`
   - Save scaler and label encoder to `models/` directory

#### Extended Dataset Preprocessing
```python
# Implementation in src/preprocessing/preprocess_extended_data.py
```

1. **Data Loading and Cleaning**
   - Load CSV file
   - Handle missing values with mean imputation
   - Convert column names to lowercase for consistency
   - Fix inconsistent naming conventions

2. **Feature Engineering**
   - Calculate average seasonal temperatures
   - Aggregate precipitation data
   - Scale numeric features
   - One-hot encode categorical features

3. **Feature Selection**
   - Correlation analysis to identify redundant features
   - Remove highly correlated features
   - Keep most informative features based on feature importance

4. **Data Splitting**
   - 80% training, 20% testing
   - Stratified split to maintain class distribution

5. **Data Storage**
   - Save processed data to `data/processed/extended_crop_recommendation_data.csv`
   - Save preprocessor and label encoder

#### Combined Dataset Processing
```python
# Implementation in src/preprocessing/preprocess_combined_data.py
```

1. **Dataset Integration**
   - Align feature names between datasets
   - Add missing features to basic dataset using seasonal averages
   - Merge datasets while avoiding duplicates

2. **Processing Combined Data**
   - Standardize all features
   - Harmonize crop label categories
   - Apply the same train/test split strategy

3. **Data Storage**
   - Save combined dataset to `data/processed/combined_crop_data.csv`
   - Save combined preprocessor for inference

### 2. Field Image Preprocessing

```python
# Implementation in src/preprocessing/process_field_dataset.py
```

1. **Image Loading and Validation**
   - Verify image integrity
   - Check for corrupt or missing images
   - Validate label and mask correspondence

2. **Image Preprocessing**
   - Resize to 224×224 pixels for model input
   - Normalize pixel values to [0, 1]
   - Apply standard ImageNet normalization

3. **Label Processing**
   - Convert categorical labels to one-hot encoding
   - Create label masks for segmentation tasks

4. **Data Augmentation**
   - Random horizontal/vertical flips
   - Random rotations
   - Color jittering
   - Random crops

5. **Dataset Creation**
   - Create training, validation, and test sets
   - Create DataLoader objects for model training
   - Save processed data to `data/processed/field_dataset/`

## Preprocessing Results

### Crop Data Statistics

| Metric | Basic Dataset | Extended Dataset | Combined Dataset |
|--------|--------------|-----------------|-----------------|
| Samples | 2,200 | 3,867 | 6,067 |
| Features | 7 | 29 | 7 (common) |
| Classes | 22 | 12 | 31 |
| Missing Values | 0% | 1.2% | 0.4% |

### Field Image Statistics

| Metric | Value |
|--------|-------|
| Total Images | 7,000+ |
| Image Size | 224×224 pixels |
| Classes | 9 |
| Train/Val/Test Split | 70%/15%/15% |

## Visualizations

Key visualizations generated during preprocessing:

1. **Feature Distributions**: Histograms and box plots for all numeric features
2. **Correlation Matrix**: Heatmap showing feature correlations
3. **Class Distribution**: Bar charts showing crop class distributions
4. **Sample Images**: Example field images with labels and masks

## Challenges and Solutions

1. **Class Imbalance**
   - **Challenge**: Uneven distribution of crop classes
   - **Solution**: Stratified sampling to maintain class proportions
   
2. **Feature Scale Differences**
   - **Challenge**: Features with widely different scales
   - **Solution**: StandardScaler to normalize all features
   
3. **Missing Values in Extended Dataset**
   - **Challenge**: Scattered missing values in extended dataset
   - **Solution**: Mean imputation for numeric features
   
4. **Inconsistent Label Names**
   - **Challenge**: Different crop naming conventions between datasets
   - **Solution**: Standardized naming convention and mapping table
   
5. **Image Quality Issues**
   - **Challenge**: Some blurry or partially obscured field images
   - **Solution**: Filtering out low-quality images, data augmentation

## Usage

To run the preprocessing pipeline:

```bash
# For crop recommendation data
python src/preprocessing/preprocess_data.py

# For field image data
python src/preprocessing/process_field_dataset.py --data_dir data2017_miniscale --output_dir data/processed/field_dataset
```

## Conclusion

The preprocessing steps significantly improved data quality and prepared it for effective model training. Key improvements include:

- Standardized feature scales
- Integrated complementary datasets
- Structured image data for deep learning
- Eliminated missing values and inconsistencies
- Created reproducible train/test splits 