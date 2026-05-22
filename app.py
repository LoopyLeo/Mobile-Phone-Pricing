import streamlit as st
import pickle
import numpy as np

# load model + scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("📱 Mobile Price Prediction")

st.write("Enter mobile specifications")

battery_power = st.number_input("Battery Power")
blue = st.selectbox("Bluetooth (0/1)", [0, 1])
clock_speed = st.number_input("Clock Speed")
dual_sim = st.selectbox("Dual SIM (0/1)", [0, 1])
fc = st.number_input("Front Camera")
four_g = st.selectbox("4G (0/1)", [0, 1])
int_memory = st.number_input("Internal Memory")
m_dep = st.number_input("Mobile Depth")
mobile_wt = st.number_input("Weight")
n_cores = st.number_input("Cores")
pc = st.number_input("Primary Camera")
px_height = st.number_input("Pixel Height")
px_width = st.number_input("Pixel Width")
ram = st.number_input("RAM")
sc_h = st.number_input("Screen Height")
sc_w = st.number_input("Screen Width")
talk_time = st.number_input("Talk Time")
three_g = st.selectbox("3G (0/1)", [0, 1])
touch_screen = st.selectbox("Touch Screen (0/1)", [0, 1])
wifi = st.selectbox("WiFi (0/1)", [0, 1])

if st.button("Predict"):

    input_data = np.array([[
        battery_power, blue, clock_speed, dual_sim, fc, four_g,
        int_memory, m_dep, mobile_wt, n_cores, pc,
        px_height, px_width, ram, sc_h, sc_w,
        talk_time, three_g, touch_screen, wifi
    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]

    price_map = {
        0: "Low Cost",
        1: "Medium Cost",
        2: "High Cost",
        3: "Very High Cost"
    }

    st.success(f"Predicted Price Range: {price_map[prediction]}")