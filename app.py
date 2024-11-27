
import streamlit as st
import time
from random import uniform

# Gas concentration thresholds (in ppm)
THRESHOLDS = {
    "CO2": 1000,  # CO2 threshold in ppm
    "CH4": 5,     # CH4 threshold in ppm
    "O3": 0.07    # Ozone threshold in ppm
}

# Function to read sensor data
def read_sensor_data():
    # Simulated sensor readings (replace with real sensor data)
    CO2 = round(uniform(400, 1200), 2)  # Simulated CO2 data
    CH4 = round(uniform(0.1, 10), 2)   # Simulated CH4 data
    O3 = round(uniform(0.01, 0.1), 3)  # Simulated O3 data
    return {"CO2": CO2, "CH4": CH4, "O3": O3}

# Function to check thresholds and generate warnings
def check_thresholds(data):
    warnings = []
    for gas, value in data.items():
        if value > THRESHOLDS[gas]:
            warnings.append(f"⚠️ WARNING: {gas} concentration is {value} ppm (exceeds {THRESHOLDS[gas]} ppm)!")
    return warnings

# Streamlit app
st.title("Greenhouse Gas Monitoring System 🌱")
st.write("This app monitors CO2, CH4, and O3 concentrations in real-time.")

# Button to fetch and display sensor data
if st.button("Fetch Sensor Data"):
    sensor_data = read_sensor_data()
    st.write(f"Sensor Data: {sensor_data}")

    # Display warnings if thresholds are exceeded
    warnings = check_thresholds(sensor_data)
    if warnings:
        for warning in warnings:
            st.warning(warning)
    else:
        st.success("✅ All gas levels are within safe limits.")
