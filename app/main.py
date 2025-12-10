# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import uvicorn

# 1. Load the trained model
try:
    model = joblib.load("model/exam_score_model.pkl")
except:
    # Fallback for testing if file doesn't exist
    print("Model file not found. Make sure 'exam_score_model.pkl' is in the folder.")
    model = None

# 2. Define the input data format
class StudentData(BaseModel):
    study_hours: float
    class_attendance: float
    sleep_hours: float
    study_method: str
    sleep_quality: str

# 3. Create the API
app = FastAPI(title="Exam Score Prediction API")


@app.post("/predict")
def predict_score(data: StudentData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Convert incoming JSON to DataFrame
    input_data = pd.DataFrame([{
        'study_hours': data.study_hours,
        'class_attendance': data.class_attendance,
        'sleep_hours': data.sleep_hours,
        'study_method': data.study_method,
        'sleep_quality': data.sleep_quality
    }])

    # Make prediction
    try:
        prediction = model.predict(input_data)

        final_score = np.clip(prediction, 0, 100)  # Ensure score is between 0 and 100
        return {"predicted_score": round(float(final_score[0]), 2)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)