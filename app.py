import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("💼 Student Salary Prediction")

st.write("Fill all details carefully 👇")

# ========== INPUTS ==========

age = st.number_input("Age", 18, 30)

gender = st.selectbox("Gender", ["Male", "Female"])
cgpa = st.number_input("CGPA", 0.0, 10.0)

branch = st.selectbox("Branch", ["IT", "CSE", "EEE", "Civil", "Mechanical", "ECE"])
college_tier = st.selectbox("College Tier", ["Tier 1", "Tier 2", "Tier 3"])

internships = st.number_input("Internships Count", 0)
projects = st.number_input("Projects Count", 0)
certifications = st.number_input("Certifications Count", 0)

coding = st.number_input("Coding Skill Score", 0.0, 100.0)
aptitude = st.number_input("Aptitude Score", 0.0, 100.0)
communication = st.number_input("Communication Score", 0.0, 100.0)
logical = st.number_input("Logical Reasoning Score", 0.0, 100.0)

hackathons = st.number_input("Hackathons Participated", 0)
github = st.number_input("GitHub Repos", 0)
linkedin = st.number_input("LinkedIn Connections", 0)

mock = st.number_input("Mock Interview Score", 0.0, 100.0)
attendance = st.number_input("Attendance %", 0.0, 100.0)

backlogs = st.number_input("Backlogs", 0)
extra = st.number_input("Extracurricular Score", 0.0, 100.0)
leadership = st.number_input("Leadership Score", 0.0, 100.0)

volunteer = st.selectbox("Volunteer Experience", ["Yes", "No"])

sleep = st.number_input("Sleep Hours", 0.0, 24.0)
study = st.number_input("Study Hours per Day", 0.0, 24.0)

placement = st.selectbox("Placement Status", ["Placed", "Not Placed"])


# ========== ENCODING (same as training) ==========

gender = 1 if gender == "Male" else 0

branch_map = {"IT":1, "CSE":2, "EEE":3, "Civil":4, "Mechanical":5, "ECE":6}
branch = branch_map[branch]

tier_map = {"Tier 1":1, "Tier 2":2, "Tier 3":3}
college_tier = tier_map[college_tier]

volunteer = 1 if volunteer == "Yes" else 0
placement = 1 if placement == "Placed" else 0


# ========== PREDICTION ==========

if st.button("Predict Salary 💰"):

    features = np.array([[age, gender, cgpa, branch, college_tier,
                          internships, projects, certifications,
                          coding, aptitude, communication, logical,
                          hackathons, github, linkedin, mock,
                          attendance, backlogs, extra, leadership,
                          volunteer, sleep, study, placement]])

    prediction = model.predict(features)

    st.success(f"💰 Predicted Salary: {prediction[0]:.2f} LPA")
