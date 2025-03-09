import joblib
import pandas as pd

# Load the saved model
model = joblib.load('random_forest_pipeline.pkl')
# Define new data (replace values with actual inputs)
new_data = pd.DataFrame([{
    'age': 25,
    'gender': 1,  # Example: 1 for Male, 0 for Female (depends on how you encoded gender)
    'weight_kg': 70,
    'body fat_%': 18.5,
    'diastolic': 80,
    'sit and bend forward_cm': 15,
    'sit-ups counts': 30,
    'broad jump_cm': 200
}])

# Ensure the column order matches the training data
# (If necessary, reorder using new_data = new_data[columns_order])
# Make predictions
prediction = model.predict(new_data)

print("Predicted class:", prediction[0])
