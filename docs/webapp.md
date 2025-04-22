# Web Applications

This document outlines the three Streamlit web applications developed for the Smart Farming project. These interactive applications allow users to analyze field conditions and get crop recommendations based on soil and climate data.

## Overview

The Smart Farming project includes three separate web applications:

1. **Field Analyzer**: Analyzes field images to identify conditions like weed clusters, water, storm damage, etc.
2. **Basic Crop Recommender**: Provides crop recommendations based on basic soil properties and climate data
3. **Advanced Crop Recommender**: Uses an extended dataset with more features for more comprehensive recommendations

## 1. Field Analyzer

**File**: `src/webapp/app.py`

### Features

- Upload field images for analysis
- Process images using a trained ResNet model
- Display predictions with confidence levels
- Visualize class probabilities with bar charts
- Provide detailed information about detected field conditions
- Show management recommendations for each condition

### Usage Flow

1. User uploads a field image
2. The app preprocesses the image and runs it through the model
3. The app displays the predicted field condition with confidence
4. The app shows a probability breakdown for all possible conditions
5. The app provides detailed information about the condition and recommended actions

### Technical Implementation

- Loads the ResNet model from `models/field_classifier/`
- Uses PyTorch for model inference
- Processes images using torchvision transformations
- Uses Streamlit components for interactive UI
- Provides fallback sample images when no image is uploaded

## 2. Basic Crop Recommender

**File**: `src/webapp/crop_recommendation_app.py`

### Features

- Input form for soil properties and climate data
- Predictions using Random Forest model
- Display of top 3 recommended crops with confidence levels
- Visualization of recommendation probabilities
- Detailed information about recommended crops

### Usage Flow

1. User enters soil properties (N, P, K, pH) and climate data (temperature, humidity, rainfall)
2. The app processes the input and runs it through the model
3. The app displays the top recommended crop with confidence
4. The app shows a bar chart of top 3 recommendations
5. The app provides detailed information about the recommended crop

### Technical Implementation

- Loads the Random Forest model from `models/random_forest_model.pkl`
- Uses scikit-learn for model inference
- Preprocesses input data using the saved scaler
- Handles label encoding/decoding with fallback mechanisms

## 3. Advanced Crop Recommender

**File**: `src/webapp/combined_model_app.py`

### Features

- Similar input form to the basic recommender
- Uses the combined model for predictions
- Displays top 5 recommendations
- Shows environmental assessment based on input values
- Visualizes soil nutrient levels
- Provides more detailed crop information

### Usage Flow

1. User enters soil and climate data
2. The app processes the input using the combined model
3. The app displays the top recommended crop with confidence
4. The app shows an environmental assessment of the soil and climate conditions
5. The app visualizes soil nutrient levels and provides detailed crop information

### Technical Implementation

- Loads the Combined Random Forest model from `models/random_forest_combined.pkl`
- Uses same underlying mechanisms as the basic recommender
- Provides more comprehensive visualization and analysis
- Implements fallback mechanisms for label encoding

## Running the Applications

### Running Individual Apps

Each application can be run individually:

```bash
# Field Analyzer
streamlit run src/webapp/app.py

# Basic Crop Recommender
streamlit run src/webapp/crop_recommendation_app.py

# Advanced Crop Recommender
streamlit run src/webapp/combined_model_app.py
```

### Running All Apps

A helper script is provided to run all three applications simultaneously:

```bash
python run_all_apps.py
```

This script:
- Starts each app on a different port:
  - Field Analyzer: http://localhost:8501
  - Basic Crop Recommender: http://localhost:8502
  - Advanced Crop Recommender: http://localhost:8503
- Opens each app in a browser tab
- Monitors all processes and shows any errors
- Handles graceful shutdown on keyboard interrupt

## UI/UX Design

All applications follow a consistent design language:

- Clean, modern interface with a dark theme
- Clear separation of input and results sections
- Interactive widgets for data input
- Visualizations to enhance understanding
- Detailed information sections
- Responsive layout using Streamlit's column system

## Error Handling

The applications include robust error handling:

- Input validation for all form fields
- Graceful handling of missing models
- Fallback mechanisms for label encoding
- Clear error messages when issues occur
- Helpful instructions for troubleshooting

## Future Enhancements

Planned improvements for the web applications:

- Integration with weather APIs for automatic climate data retrieval
- Geolocation support for location-specific recommendations
- Ability to save and compare multiple recommendations
- PDF report generation
- Mobile-optimized interface
- User accounts and history tracking 