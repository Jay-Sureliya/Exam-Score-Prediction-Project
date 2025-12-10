🎓 Exam Score Prediction System (ML + FastAPI + Streamlit)

This project predicts a student’s exam score (0–100) using their study habits, attendance, sleep patterns, and study methods.
The system includes:

📌 Machine Learning Model (Linear Regression + Pipeline)

🚀 FastAPI Backend API

🌐 Streamlit Frontend UI

💾 Model Saved with Joblib

| Component   | Technology                   |
| ----------- | ---------------------------- |
| Data / ML   | Pandas, Scikit-Learn, Joblib |
| Backend API | FastAPI, Uvicorn, Pydantic   |
| Frontend    | Streamlit                    |
| Others      | Requests, NumPy              |


📁 Project Structure

Exam Score Prediction/
├── app/
│   ├── main.py          # FastAPI Backend (The Brain)
│   └── app.py           # Streamlit Frontend (The Interface)
├── data/
│   └── Exam_Score_Prediction.csv        # Raw Dataset
├── model/
│   └── exam_score_model.pkl  # Trained Model Artifact
├── src/
│   └── train_model.py   # Script to train and save the model
├── requirements.txt     # Dependencies
└── README.md            # Project Documentation


⚙️ How It Works

1️⃣ ML training (train_model.py)
✔️ Cleans data
✔️ Scales numeric values
✔️ One-Hot Encodes categories
✔️ Builds pipeline
✔️ Saves final model as .pkl

2️⃣ Backend API (main.py)
✔️ Loads saved model
✔️ Accepts JSON input
✔️ Returns predicted exam score

3️⃣ Frontend (app.py)
✔️ Sends data to API
✔️ Displays score & performance insights

▶️ Run the Project
🔹 Install Requirements
pip install -r requirements.txt

🔹 Train the Model
python train_model.py

🔹 Start FastAPI Backend
uvicorn main:app --reload

🔹 Run Streamlit Frontend
streamlit run app.py


⚠ Make sure the FastAPI server is running before opening Streamlit.

📌 Example API Request
{
  "study_hours": 5,
  "class_attendance": 80,
  "sleep_hours": 7,
  "study_method": "self-study",
  "sleep_quality": "good"
}

📈 Future Improvements

🔧 Add Feature Scaling Options
🎯 Try RandomForest/XGBoost for comparison
📊 Add confidence intervals or error metrics
🧩 Add login system to save user history
📱 Deploy on cloud (Render / Railway / HuggingFace)

👨‍💻 Author

Developed by Jay Sureliya