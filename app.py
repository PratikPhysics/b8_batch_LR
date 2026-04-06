import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Iris Classifier", layout="centered")

st.title("🌸 Iris Flower Prediction App")
st.write("Predict the species of Iris flower using AdaBoost model")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, step=0.1)

# Prediction
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)

    # Mapping output (depends on your encoding)
    species = ["Setosa", "Versicolor", "Virginica"]

    st.success(f"🌼 Predicted Species: {species[prediction[0]]}")
