
# 🏠 AI-Based Smart Home Energy Recommendation System

## 📌 Project Description

The AI-Based Smart Home Energy Recommendation System is a
Machine Learning project designed to reduce electricity wastage
in homes.

It analyses room temperature, occupancy, lighting conditions,
and appliance usage to recommend whether lights, fans, and
other appliances should be switched ON or OFF.

The system uses Decision Tree Classification and displays
recommendations through a Streamlit dashboard.

---

## 🎯 Objectives

1. Reduce unnecessary electricity consumption.
2. Analyse room temperature and occupancy.
3. Recommend light and fan settings.
4. Apply Machine Learning algorithms.
5. Estimate electricity and cost savings.
6. Display results using a dashboard.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib

---

## 📂 Project Structure

```text
AI_Smart_Home_Energy/
│
├── app.py
├── generate_dataset.py
├── train_model.py
├── smart_home_energy_data.csv
├── smart_home_model.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

The project uses a synthetic dataset containing
500 smart-home records.

### Input Features

- Temperature
- Occupancy
- Light Lux
- Appliance Usage Hours

### Output Features

- Light Status
- Fan Status
- Appliance Status

---

## 🤖 Machine Learning Algorithm

Decision Tree Classification is used to predict
the appliance recommendations.

Three separate models are trained:

1. Light Recommendation Model
2. Fan Recommendation Model
3. Appliance Recommendation Model

---

## ⚙️ Installation

### Step 1: Install Python Libraries

```bash
pip install -r requirements.txt
```

### Step 2: Generate Dataset

```bash
python generate_dataset.py
```

### Step 3: Train Machine Learning Model

```bash
python train_model.py
```

### Step 4: Run Streamlit Application

```bash
streamlit run app.py
```

---

## 💡 Project Features

- Smart light ON/OFF recommendations.
- Smart fan ON/OFF recommendations.
- Appliance usage recommendations.
- Temperature monitoring through user input.
- Occupancy analysis.
- Energy-saving calculation.
- Electricity cost estimation.
- Interactive Streamlit dashboard.
- Graphical energy-saving visualization.
- Downloadable energy report.

---

## 📈 Energy Saving Formula

Energy Consumption (kWh) =

(Power in Watts × Usage Hours) / 1000

Estimated Money Saved =

Energy Saved × Electricity Tariff

---

## 🏠 Applications

- Smart Homes
- Residential Buildings
- Energy Management
- Electricity Conservation
- Smart Building Systems

---

## 🔮 Future Enhancements

1. Integration with real IoT sensors.
2. Real-time electricity monitoring.
3. Automatic smart appliance control.
4. Mobile application integration.
5. Advanced Machine Learning models.

---

## 📝 Conclusion

The AI-Based Smart Home Energy Recommendation System
helps users understand and reduce unnecessary electricity
consumption through intelligent recommendations.

It uses Machine Learning to analyse simulated room
conditions and provides energy-saving suggestions
through an interactive dashboard.

---

## ⚠️ Disclaimer

This project is a simulation using synthetic data.
It does not control real electrical appliances.
Energy savings are estimated using configurable
appliance power ratings and usage assumptions.
