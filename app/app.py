import streamlit as st
import pandas as pd
import pickle
import os

# -------------------------------
# LOAD MODEL (WORKS EVERYWHERE)
# -------------------------------
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "pipeline_model.pkl")
model = pickle.load(open(model_path, "rb"))

# -------------------------------
# UI
# -------------------------------
st.title("🚀 Employee Performance Prediction System")
st.markdown("Predict employee performance using Machine Learning")

st.write("### Enter Employee Details:")

# -------------------------------
# INPUT FIELDS
# -------------------------------
data = {
    "Age": st.slider("Age", 18, 60, 30),
    "Gender": st.selectbox("Gender", ["Male", "Female"]),
    "EducationBackground": st.selectbox(
        "Education Background",
        ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"]
    ),
    "MaritalStatus": st.selectbox("Marital Status", ["Single", "Married", "Divorced"]),
    "EmpDepartment": st.selectbox(
        "Department",
        ["Sales", "Development", "Research & Development", "Human Resources", "Finance"]
    ),
    "EmpJobRole": st.text_input("Job Role", "Developer"),
    "BusinessTravelFrequency": st.selectbox(
        "Travel Frequency",
        ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    ),
    "DistanceFromHome": st.slider("Distance From Home", 1, 50, 10),
    "EmpEducationLevel": st.slider("Education Level", 1, 5, 3),
    "EmpEnvironmentSatisfaction": st.slider("Environment Satisfaction", 1, 4, 3),
    "EmpHourlyRate": st.slider("Hourly Rate", 30, 150, 70),
    "EmpJobInvolvement": st.slider("Job Involvement", 1, 4, 3),
    "EmpJobLevel": st.slider("Job Level", 1, 5, 2),
    "EmpJobSatisfaction": st.slider("Job Satisfaction", 1, 4, 3),
    "NumCompaniesWorked": st.slider("Companies Worked", 0, 10, 2),
    "OverTime": st.selectbox("OverTime", ["Yes", "No"]),
    "EmpLastSalaryHikePercent": st.slider("Salary Hike (%)", 10, 30, 15),
    "EmpRelationshipSatisfaction": st.slider("Relationship Satisfaction", 1, 4, 3),
    "TotalWorkExperienceInYears": st.slider("Total Experience", 0, 40, 5),
    "TrainingTimesLastYear": st.slider("Training Times Last Year", 0, 10, 2),
    "EmpWorkLifeBalance": st.slider("Work Life Balance", 1, 4, 3),
    "ExperienceYearsAtThisCompany": st.slider("Years at Company", 0, 20, 5),
    "ExperienceYearsInCurrentRole": st.slider("Years in Role", 0, 20, 3),
    "YearsSinceLastPromotion": st.slider("Years Since Last Promotion", 0, 15, 2),
    "YearsWithCurrManager": st.slider("Years with Manager", 0, 15, 3),
    "Attrition": st.selectbox("Attrition", ["Yes", "No"])
}

# -------------------------------
# CONVERT TO DATAFRAME
# -------------------------------
input_df = pd.DataFrame([data])

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict Performance"):
    prediction = model.predict(input_df)[0]

    if prediction == 2:
        st.error("🔴 Low Performance Employee")
    elif prediction == 3:
        st.warning("🟡 Average Performance Employee")
    else:
        st.success("🟢 High Performance Employee")