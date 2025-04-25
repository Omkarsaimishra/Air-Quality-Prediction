import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model/Regressor_model.sav', 'rb'))

# Title
st.title("Air Quality Prediction")

# User input fields
time = st.number_input('Time', value=0.0)
CO_GT = st.number_input('CO_GT', value=0.0)
C6h_GT = st.number_input('C6H_GT', value=0.0)
PT08_S2 = st.number_input('PT08_S2', value=0.0)
NOx = st.number_input('NOx', value=0.0)
PT08_S3 = st.number_input('PT08_S3', value=0.0)
NO2x = st.number_input('NO2x', value=0.0)
PT08_s4 = st.number_input('PT08_s4', value=0.0)
PT08_s5 = st.number_input('PT08_s5', value=0.0)
T = st.number_input('Temperature (T)', value=0.0)
AH = st.number_input('Absolute Humidity (AH)', value=0.0)

# When the user clicks the Predict button
if st.button("Predict"):
    input_data = np.array([[time, CO_GT, C6h_GT, PT08_S2, NOx, PT08_S3, NO2x, PT08_s4, PT08_s5, T, AH]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Air Quality Value: {prediction[0]:.2f}")
