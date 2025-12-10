# app.py
import streamlit as st
import requests
import time

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="Exam Success AI",
    page_icon="🎓",
    layout="centered"
)

# --- Custom Styling (Optional) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
    }
    .result-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3406/3406986.png", width=100)
    st.header("About the Model")
    st.write("""
    This AI tool predicts your potential exam score based on:
    - 📚 Study Habits
    - 😴 Sleep Patterns
    - 🏫 Attendance
    """)
    st.info("💡 Tip: Consistency is key! Regular study hours often outweigh last-minute cramming.")

# --- Main Content ---
st.title("🎓 Exam Score Predictor")
st.markdown("### optimize your routine for better grades.")
st.divider()

# --- Input Form ---
with st.form("prediction_form"):
    
    st.subheader("1. Academic Stats")
    col1, col2 = st.columns(2)
    
    with col1:
        study_hours = st.slider(
            "📚 Study Hours (Daily)", 
            min_value=0.0, max_value=20.0, value=5.0, step=0.5,
            help="Average hours spent studying per day."
        )
    
    with col2:
        class_attendance = st.slider(
            "🏫 Class Attendance (%)", 
            min_value=0.0, max_value=100.0, value=85.0,
            help="Percentage of classes attended."
        )

    st.subheader("2. Lifestyle & Strategy")
    col3, col4 = st.columns(2)

    with col3:
        sleep_hours = st.number_input(
            "😴 Sleep Hours", 
            min_value=0.0, max_value=12.0, value=7.0, step=0.5
        )
        
        sleep_quality = st.radio(
            "🛏️ Sleep Quality", 
            options=['poor', 'average', 'good'],
            index=1,
            horizontal=True
        )

    with col4:
        study_method = st.selectbox(
            "🧠 Primary Study Method", 
            ['coaching', 'online videos', 'mixed', 'self-study', 'group study'],
            index=2
        )

    st.markdown("---")
    
    # Submit Button
    submitted = st.form_submit_button("🚀 Predict My Score")

# --- Logic when button is clicked ---
if submitted:
    # Prepare payload
    payload = {
        "study_hours": study_hours,
        "class_attendance": class_attendance,
        "sleep_hours": sleep_hours,
        "study_method": study_method,
        "sleep_quality": sleep_quality
    }

    # Spinner for effect
    with st.spinner("Analyzing your data..."):
        time.sleep(1) # Artificial delay for UX effect
        
        try:
            # Call FastAPI
            response = requests.post("http://127.0.0.1:8000/predict", json=payload)
            
            if response.status_code == 200:
                result = response.json()
                score = result["predicted_score"]

                # --- Display Results ---
                st.balloons()
                
                # Create a metric card
                st.markdown("<br>", unsafe_allow_html=True)
                col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
                
                with col_res2:
                    st.metric(label="Predicted Exam Score", value=f"{score}/100")
                    
                    # Visual Progress Bar
                    st.progress(score / 100)
                    
                    # Contextual Message
                    if score >= 80:
                        st.success("🌟 Excellent! You are on track for a distinction.")
                    elif score >= 50:
                        st.warning("⚠️ Good, but there is room for improvement.")
                    else:
                        st.error("🚨 Warning: You might need to change your strategy.")

            else:
                st.error(f"Server Error: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("🚨 Connection Error: Cannot connect to the backend. Is 'main.py' running?")