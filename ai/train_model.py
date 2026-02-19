import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

DATA_PATH = "ai/deployment_history.csv"
MODEL_PATH = "ai/deployment_model.pkl"

# ---------------------------------------------------
# 1️⃣ Ensure Dataset Exists (Auto-create if missing)
# ---------------------------------------------------
if not os.path.exists(DATA_PATH):
    print("Dataset not found. Creating new dataset.")
    df = pd.DataFrame(columns=[
        "lines_changed",
        "files_changed",
        "commit_message_length",
        "churn_rate",
        "failed"
    ])
    df.to_csv(DATA_PATH, index=False)

data = pd.read_csv(DATA_PATH)

# ---------------------------------------------------
# 2️⃣ If Not Enough Data → Create Baseline Model
# ---------------------------------------------------
if len(data) < 5:
    print("Not enough data. Creating baseline model.")

    model = RandomForestClassifier(n_estimators=10)

    # Minimal synthetic training data
    X_dummy = [[0, 0, 0, 0]]
    y_dummy = [0]

    model.fit(X_dummy, y_dummy)
    joblib.dump(model, MODEL_PATH)

    print("Baseline model created successfully.")
    exit()

# ---------------------------------------------------
# 3️⃣ Normal Training
# ---------------------------------------------------
X = data.drop("failed", axis=1)
y = data["failed"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, MODEL_PATH)

print("Model trained successfully.")
