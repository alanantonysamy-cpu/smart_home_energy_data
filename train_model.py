
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("smart_home_energy_data.csv")

X = df[
    ["temperature", "occupancy",
     "light_lux", "usage_hours"]
]

targets = [
    "light_status",
    "fan_status",
    "appliance_status"
]

models = {}
accuracies = {}

# Train three models
for target in targets:

    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    models[target] = model
    accuracies[target] = accuracy

    print(target, "Accuracy:", round(accuracy * 100, 2), "%")

# Save trained models
joblib.dump(
    {
        "models": models,
        "accuracies": accuracies
    },
    "smart_home_model.pkl"
)

print("Machine Learning model saved successfully!")
