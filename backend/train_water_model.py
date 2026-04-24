import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def train_model():
    data_path = os.path.join(os.path.dirname(__file__), 'water_data.csv')
    if not os.path.exists(data_path):
        print("Data file not found.")
        return

    df = pd.read_csv(data_path)

    # Features: pH + all chemical binary columns
    chemicals_list = ['Lead', 'Mercury', 'Arsenic', 'Fluoride', 'Pesticides', 'Bacteria']
    feature_cols = ['ph'] + chemicals_list
    
    X = df[feature_cols]
    y_treatment = df['treatment']
    y_disease = df['disease']

    X_train, X_test, y_train_t, y_test_t = train_test_split(X, y_treatment, test_size=0.2, random_state=42)
    _, _, y_train_d, y_test_d = train_test_split(X, y_disease, test_size=0.2, random_state=42)

    rf_params = {
        'n_estimators': 150,
        'max_depth': 12,
        'min_samples_leaf': 2,
        'random_state': 42
    }

    model_treatment = RandomForestClassifier(**rf_params)
    model_treatment.fit(X_train, y_train_t)

    model_disease = RandomForestClassifier(**rf_params)
    model_disease.fit(X_train, y_train_d)

    # Evaluate
    train_acc_t = accuracy_score(y_train_t, model_treatment.predict(X_train))
    test_acc_t = accuracy_score(y_test_t, model_treatment.predict(X_test))
    
    print(f"Treatment Model - Train Acc: {train_acc_t*100:.2f}%, Test Acc: {test_acc_t*100:.2f}%")

    # Save
    model_dir = os.path.dirname(__file__)
    joblib.dump(model_treatment, os.path.join(model_dir, 'model_treatment.pkl'))
    joblib.dump(model_disease, os.path.join(model_dir, 'model_disease.pkl'))
    # Save the feature columns list to ensure consistency in app.py
    joblib.dump(feature_cols, os.path.join(model_dir, 'feature_cols.pkl'))

    print("Models updated for multi-chemical support.")

if __name__ == "__main__":
    train_model()
