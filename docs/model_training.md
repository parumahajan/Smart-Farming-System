# Model Training

This document outlines the model training process for the Smart Farming project. We trained several machine learning models for crop recommendation and field condition analysis.

## 1. Crop Recommendation Models

### Basic Random Forest Model

```python
# Implementation in src/training/crop_prediction_model.py
```

- **Input Data**: Processed basic crop recommendation dataset
- **Features**: 7 (N, P, K, temperature, humidity, pH, rainfall)
- **Classes**: 22 crop types
- **Model**: Random Forest Classifier
- **Hyperparameters**:
  - `n_estimators`: 100
  - `random_state`: 42
  - Other parameters: default
- **Training Process**:
  - Trained on 80% of data (1,760 samples)
  - 5-fold cross-validation for hyperparameter tuning
- **Output**: `models/random_forest_model.pkl`

### Combined Random Forest Model

```python
# Implementation in src/training/train_combined_model.py
```

- **Input Data**: Combined crop recommendation dataset
- **Features**: 7 common features
- **Classes**: 31 crop types
- **Model**: Random Forest Classifier
- **Hyperparameters**:
  - `n_estimators`: 100
  - `random_state`: 42
  - Other parameters: default
- **Training Process**:
  - Trained on 80% of combined data (~4,853 samples)
  - No hyperparameter tuning to maintain comparability
- **Output**: `models/random_forest_combined.pkl`

### Extended Model with All Features

```python
# Implementation in src/training/train_combined_model.py
```

- **Input Data**: Extended crop recommendation dataset
- **Features**: 75 (after one-hot encoding)
- **Classes**: 12 crop types
- **Model**: Random Forest Classifier
- **Hyperparameters**: Same as combined model
- **Training Process**:
  - Trained on 80% of extended data (~3,093 samples)
  - No hyperparameter tuning to maintain comparability
- **Output**: `models/random_forest_extended.pkl`

## 2. Field Condition Classifier

```python
# Implementation in src/training/field_classifier.py
```

- **Input Data**: Processed field image dataset
- **Architecture**: ResNet-18
- **Input Size**: 224×224×3 RGB images
- **Output Classes**: 9 field conditions
- **Transfer Learning**:
  - Pretrained on ImageNet
  - Fine-tuned on our field dataset
- **Training Configuration**:
  - Batch size: 32
  - Learning rate: 0.001
  - Optimizer: Adam
  - Loss function: Cross-Entropy
  - Epochs: 3
- **Data Augmentation**:
  - Random horizontal/vertical flips
  - Random rotations
  - Color jittering
- **Output**: `models/field_classifier/resnet_20250419_044617/best_model.pth`

## Model Evaluation

### Crop Recommendation Models

| Metric | Basic Model | Combined Model | Extended Model |
|--------|------------|----------------|----------------|
| Accuracy | ~90% | 67.30% | 51.68% |
| Precision (macro) | 0.91 | 0.73 | 0.23 |
| Recall (macro) | 0.89 | 0.72 | 0.21 |
| F1 Score (macro) | 0.90 | 0.72 | 0.21 |

### Field Condition Classifier

- **Accuracy**: ~75% on test set
- **Best performing classes**: water, weed_cluster, storm_damage
- **Challenging classes**: nutrient_deficiency, planter_skip

## Analysis and Insights

### Performance Comparison

- The basic model shows the highest accuracy, likely due to having a more balanced dataset with fewer classes
- The combined model performs well considering the increased class count and data diversity
- The extended model has lower accuracy, likely due to the high dimensionality and fewer samples per class

### Feature Importance

In the crop recommendation models, the most important features were:
1. Rainfall
2. Temperature 
3. Humidity
4. Nitrogen content
5. pH value

### Error Analysis

Common misclassifications:
- Similar crops with overlapping growing conditions
- Crops with small representation in the training data
- Field conditions with subtle visual differences

## Usage

To train the models:

```bash
# Basic crop recommendation model
python src/training/crop_prediction_model.py

# Combined and extended models
python src/training/train_combined_model.py

# Field classifier
python src/training/field_classifier.py --dataset_dir data/processed/field_dataset --model_type resnet --epochs 3
```

## Future Improvements

- **Hyperparameter Optimization**: Grid search for optimal hyperparameters
- **Advanced Architectures**: Try ensemble methods or deep learning for crop recommendation
- **Data Augmentation**: Generate synthetic samples for underrepresented crops
- **Model Explainability**: Implement SHAP or LIME for better feature importance understanding
- **Extended Training**: Increase training epochs for the field classifier 