# Usage Guide

This guide explains how to use the Smart Farming applications for crop recommendation and field analysis.

## Running the Applications

### Option 1: All Applications at Once

To run all three applications simultaneously:

```bash
python run_all_apps.py
```

This will start:
- Field Analyzer at http://localhost:8501
- Basic Crop Recommender at http://localhost:8502
- Advanced Crop Recommender at http://localhost:8503

Each application will open in a separate browser tab.

### Option 2: Individual Applications

To run applications individually:

```bash
# Field Analyzer
streamlit run src/webapp/app.py

# Basic Crop Recommender
streamlit run src/webapp/crop_recommendation_app.py

# Advanced Crop Recommender
streamlit run src/webapp/combined_model_app.py
```

## Field Analyzer User Guide

The Field Analyzer uses computer vision to identify field conditions from aerial imagery.

### Steps to Analyze Field Images

1. **Upload an Image**
   - Click the "Browse files" button
   - Select a field image from your computer
   - Supported formats: JPG, JPEG, PNG

2. **View Results**
   - The application will process the image using the trained model
   - The predicted field condition will be displayed with a confidence score
   - A bar chart will show probabilities for all possible conditions

3. **Field Condition Information**
   - Scroll down to see detailed information about the detected condition
   - Read the description, potential impact, and recommended actions

4. **Try Different Images**
   - Upload different images to analyze various field conditions
   - Example images are provided if you don't have your own

### Sample Field Conditions

- **Double Plant**: Areas where seeds were planted too closely
- **Drydown**: Crop moisture reduction before harvest
- **Endrow**: Areas at field ends where equipment turns
- **Nutrient Deficiency**: Plants lacking essential nutrients
- **Planter Skip**: Areas where planter failed to place seeds
- **Storm Damage**: Weather-damaged crops
- **Water**: Standing water or flooding
- **Waterway**: Water flow channels
- **Weed Cluster**: Concentrated weed growth

## Basic Crop Recommender User Guide

The Basic Crop Recommender suggests crops based on soil properties and climate data.

### Steps to Get Crop Recommendations

1. **Enter Soil Data**
   - Input Nitrogen (N) content in kg/ha
   - Input Phosphorus (P) content in kg/ha
   - Input Potassium (K) content in kg/ha
   - Input pH value

2. **Enter Climate Data**
   - Input Temperature in °C
   - Input Humidity in %
   - Input Rainfall in mm

3. **Get Recommendation**
   - Click the "Get Recommendation" button
   - View the recommended crop with confidence score
   - See top 3 recommendations with probability chart

4. **Crop Information**
   - Scroll down to see detailed information about the recommended crop
   - Information includes description, growing conditions, soil requirements, and water needs

### Sample Input Values

For testing, you can use these sample values:

| Parameter | Value |
|-----------|-------|
| Nitrogen | 90 |
| Phosphorus | 42 |
| Potassium | 43 |
| Temperature | 21 |
| Humidity | 82 |
| pH | 6.5 |
| Rainfall | 103 |

Expected result: Rice (with high confidence)

## Advanced Crop Recommender User Guide

The Advanced Crop Recommender uses a combined dataset for more comprehensive recommendations.

### Steps to Get Advanced Recommendations

1. **Enter Soil and Climate Data**
   - Same input fields as the Basic Recommender
   - Input values for N, P, K, temperature, humidity, pH, and rainfall

2. **Get Recommendation**
   - Click the "Get Recommendation" button
   - View the recommended crop with confidence score
   - See top 5 recommendations with probability chart

3. **View Environmental Assessment**
   - The application evaluates your input data
   - Displays soil quality assessment
   - Shows climate suitability
   - Visualizes soil nutrient levels

4. **Crop Information**
   - View detailed information about the recommended crop
   - Information is more comprehensive than in the basic recommender

## Interpreting Results

### Field Analyzer Results

- **High Confidence (>80%)**: The model is very certain about the field condition
- **Medium Confidence (50-80%)**: The model has moderate certainty
- **Low Confidence (<50%)**: The model is uncertain; consider a manual inspection

### Crop Recommendation Results

- **High Confidence (>70%)**: Strongly recommended crop for the given conditions
- **Medium Confidence (40-70%)**: Suitable crop, but alternatives may work well too
- **Low Confidence (<40%)**: Multiple crops may be suitable; consider experimenting

## Advanced Usage

### Comparing Recommendations

Run both crop recommenders with the same input values to compare results:

1. Enter identical values in both the basic and advanced recommenders
2. Compare the recommendations and confidence levels
3. The differences reveal how the extended dataset influences predictions

### Batch Processing Field Images

For analyzing multiple field images:

1. Create a directory with all images to analyze
2. Use the Field Analyzer for each image
3. Record results in a spreadsheet for comparison

### Using API Endpoints (For Developers)

The Streamlit applications can be accessed via HTTP endpoints:

```python
import requests
import json

# Example: Basic Crop Recommender API call
data = {
    "n": 90,
    "p": 42,
    "k": 43,
    "temperature": 21,
    "humidity": 82,
    "ph": 6.5,
    "rainfall": 103
}

response = requests.post(
    "http://localhost:8502/api/predict",
    headers={"Content-Type": "application/json"},
    data=json.dumps(data)
)

result = response.json()
print(f"Recommended crop: {result['prediction']}")
print(f"Confidence: {result['confidence']}")
```

## Troubleshooting

### Application Not Working

- Ensure all required models are trained and in the correct directories
- Check for error messages in the terminal running the application
- Verify that all dependencies are installed correctly

### Poor Predictions

- Check that your input values are within reasonable ranges
- Ensure images are clear and show the field condition clearly
- Consider retraining models with additional data if consistently poor

### Slow Performance

- Field Analyzer: Resize large images before uploading
- Crop Recommenders: Usually fast, but can be slow on older hardware
- Run applications separately if running all together is too resource-intensive 