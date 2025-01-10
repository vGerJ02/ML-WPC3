import streamlit as st

def create_insurance_form():
    with st.form(key="insurance_form"):
        st.header("Enter Insurance Details")

        age = st.number_input("Age of the insured individual (18-100)", min_value=18, max_value=100, value=30)
        gender = st.selectbox("Gender of the insured individual", options=["Male", "Female"])
        annual_income = st.number_input("Annual income of the insured individual", min_value=0, value=50000)
        marital_status = st.selectbox("Marital Status", options=["Single", "Married", "Divorced"])
        dependents = st.number_input("Number of dependents", min_value=0, value=0)
        education = st.selectbox("Highest education level attained", options=["High School", "Bachelor's", "Master's", "PhD"])
        occupation = st.selectbox("Occupation", options=["Employed", "Self-Employed", "Unemployed"])
        health_score = st.slider("Health Score (0-100)", min_value=0, max_value=100, value=75)
        location = st.selectbox("Location Type", options=["Urban", "Suburban", "Rural"])
        policy_type = st.selectbox("Type of insurance policy", options=["Basic", "Comprehensive", "Premium"])
        previous_claims = st.number_input("Number of previous claims made", min_value=0, value=0)
        vehicle_age = st.number_input("Age of the vehicle insured (years)", min_value=0, value=5)
        credit_score = st.slider("Credit Score (0-850)", min_value=0, max_value=850, value=700)
        insurance_duration = st.number_input("Insurance Duration (years)", min_value=1, value=1)
        policy_start_date = st.date_input("Policy Start Date")
        customer_feedback = st.selectbox("Customer Feedback", options=["Good", "Average", "Poor", "No feedback"])
        smoking_status = st.selectbox("Smoking Status", options=["Yes", "No"])
        exercise_frequency = st.selectbox("Frequency of Exercise", options=["Daily", "Weekly", "Monthly", "Rarely"])
        property_type = st.selectbox("Property Type", options=["House", "Apartment", "Condo"])

        submitted = st.form_submit_button("Submit")

        if submitted:
            return {
                "age": age,
                "gender": gender,
                "annual_income": annual_income,
                "marital_status": marital_status,
                "dependents": dependents,
                "education": education,
                "occupation": occupation,
                "health_score": health_score,
                "location": location,
                "policy_type": policy_type,
                "previous_claims": previous_claims,
                "vehicle_age": vehicle_age,
                "credit_score": credit_score,
                "insurance_duration": insurance_duration,
                "policy_start_date": str(policy_start_date),
                "customer_feedback": customer_feedback,
                "smoking_status": smoking_status,
                "exercise_frequency": exercise_frequency,
                "property_type": property_type,
            }
    return None
