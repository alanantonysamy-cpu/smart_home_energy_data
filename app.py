
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Smart Home Energy System",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 AI-Based Smart Home Energy Recommendation System")

st.write(
    "An intelligent system to reduce electricity "
    "wastage using Machine Learning."
)

# Load trained model
if not os.path.exists("smart_home_model.pkl"):
    st.error("Model not found. Run train_model.py first.")
    st.stop()

saved = joblib.load("smart_home_model.pkl")
models = saved["models"]
accuracies = saved["accuracies"]

# Sidebar inputs
st.sidebar.header("Smart Home Settings")

temperature = st.sidebar.slider(
    "Room Temperature (°C)", 15, 45, 30
)

occupancy = st.sidebar.selectbox(
    "Room Occupancy", ["Occupied", "Empty"]
)

occupancy_value = 1 if occupancy == "Occupied" else 0

light = st.sidebar.slider(
    "Lighting Level (Lux)", 0, 1000, 200
)

usage = st.sidebar.slider(
    "Appliance Usage Hours", 0.0, 12.0, 2.0
)

st.sidebar.header("Current Appliance Status")

current_light = st.sidebar.checkbox("Light is ON", True)
current_fan = st.sidebar.checkbox("Fan is ON", True)
current_appliance = st.sidebar.checkbox(
    "Other appliance is ON", True
)

st.sidebar.header("Energy Settings")

light_power = st.sidebar.number_input(
    "Light Power (Watts)", value=15, min_value=1
)

fan_power = st.sidebar.number_input(
    "Fan Power (Watts)", value=75, min_value=1
)

appliance_power = st.sidebar.number_input(
    "Other Appliance Power (Watts)", value=100, min_value=1
)

saving_hours = st.sidebar.slider(
    "Estimated unnecessary ON time (hours)",
    0.5, 12.0, 4.0
)

rate = st.sidebar.number_input(
    "Electricity Cost (₹/kWh)",
    value=8.0,
    min_value=0.0
)

# Main prediction
if st.button("Generate Smart Recommendations"):

    input_data = pd.DataFrame([{
        "temperature": temperature,
        "occupancy": occupancy_value,
        "light_lux": light,
        "usage_hours": usage
    }])

    light_prediction = models["light_status"].predict(
        input_data
    )[0]

    fan_prediction = models["fan_status"].predict(
        input_data
    )[0]

    appliance_prediction = models["appliance_status"].predict(
        input_data
    )[0]

    st.header("💡 Smart Recommendations")

    col1, col2, col3 = st.columns(3)

    col1.metric("Light", light_prediction)
    col2.metric("Fan", fan_prediction)
    col3.metric("Appliance", appliance_prediction)

    # Explain recommendations
    st.header("🧠 Recommendation Explanation")

    if occupancy_value == 0:
        st.write("Room is empty. Lights and fans are not required.")
    else:
        if light < 300:
            st.write("Light ON: Room brightness is below 300 lux.")
        else:
            st.write("Light OFF: Sufficient natural light is available.")

        if temperature >= 28:
            st.write("Fan ON: Room temperature is 28°C or higher.")
        else:
            st.write("Fan OFF: Room temperature is below 28°C.")

        if usage >= 0.5:
            st.write("Appliance ON: Appliance usage is required.")
        else:
            st.write("Appliance OFF: No significant usage is required.")

    # Energy calculation
    st.header("⚡ Energy Saving Calculation")

    devices = [
        ("Light", light_prediction, current_light, light_power),
        ("Fan", fan_prediction, current_fan, fan_power),
        ("Appliance", appliance_prediction,
         current_appliance, appliance_power)
    ]

    results = []

    for name, prediction, current, power in devices:

        saved = 0

        if current and prediction == "OFF":
            saved = power * saving_hours / 1000

        results.append({
            "Device": name,
            "Recommendation": prediction,
            "Energy Saved (kWh)": round(saved, 3),
            "Money Saved (₹)": round(saved * rate, 2)
        })

    result_df = pd.DataFrame(results)

    st.dataframe(result_df, use_container_width=True)

    total_energy = result_df["Energy Saved (kWh)"].sum()
    total_money = result_df["Money Saved (₹)"].sum()

    c1, c2 = st.columns(2)

    c1.metric(
        "Estimated Energy Saved",
        f"{total_energy:.3f} kWh"
    )

    c2.metric(
        "Estimated Money Saved",
        f"₹{total_money:.2f}"
    )

    # Chart
    st.header("📊 Energy Saving Dashboard")

    fig, ax = plt.subplots()

    ax.bar(
        result_df["Device"],
        result_df["Energy Saved (kWh)"]
    )

    ax.set_xlabel("Appliances")
    ax.set_ylabel("Energy Saved (kWh)")
    ax.set_title("Energy Saving Analysis")

    st.pyplot(fig)
    plt.close(fig)

    # Model accuracy
    st.header("🤖 Machine Learning Model Performance")

    accuracy_df = pd.DataFrame({
        "Model": list(accuracies.keys()),
        "Accuracy (%)": [
            round(value * 100, 2)
            for value in accuracies.values()
        ]
    })

    st.dataframe(accuracy_df, use_container_width=True)

    # Download report
    st.download_button(
        "Download Energy Report",
        data=result_df.to_csv(index=False),
        file_name="energy_report.csv",
        mime="text/csv"
    )

else:
    st.info(
        "Enter your smart home conditions in the sidebar "
        "and click Generate Smart Recommendations."
    )

    st.subheader("Model Accuracy")

    st.write({
        name: f"{value * 100:.2f}%"
        for name, value in accuracies.items()
    })

st.divider()

st.caption(
    "Educational simulation only. This application does not "
    "control real-world electrical appliances."
)
