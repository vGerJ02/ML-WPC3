from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model = joblib.load('model.pkl')

# Create FastAPI instance
app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    age: int
    gender: str
    annual_income: float
    marital_status: str
    dependents: int
    education: str
    occupation: str
    health_score: int
    location: str
    policy_type: str
    previous_claims: int
    vehicle_age: int
    credit_score: int
    insurance_duration: int
    policy_start_date: str
    customer_feedback: str
    smoking_status: str
    exercise_frequency: str
    property_type: str

# Define the prediction endpoint
@app.post("/predict/")
async def predict(data: InputData):
    # Convert input data to the format expected by the model
    input_features = np.array([
        data.age,
        data.gender,  # You may need to encode categorical variables
        data.annual_income,
        data.marital_status,  # Same here
        data.dependents,
        data.education,  # Same here
        data.occupation,  # Same here
        data.health_score,
        data.location,  # Same here
        data.policy_type,  # Same here
        data.previous_claims,
        data.vehicle_age,
        data.credit_score,
        data.insurance_duration,
        # Convert date to a numerical format if needed
        data.customer_feedback,  # Same here
        data.smoking_status,  # Same here
        data.exercise_frequency,  # Same here
        data.property_type  # Same here
    ]).reshape(1, -1)  # Reshape for a single sample

    # Make prediction
    prediction = model.predict(input_features)

    return {"prediction": prediction[0]}
