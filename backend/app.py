from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import pandas as pd

app = Flask(__name__, static_folder='..', static_url_path='')
CORS(app)

# Load models and features
model_dir = os.path.dirname(__file__)
model_treatment = joblib.load(os.path.join(model_dir, 'model_treatment.pkl'))
model_disease = joblib.load(os.path.join(model_dir, 'model_disease.pkl'))
feature_cols = joblib.load(os.path.join(model_dir, 'feature_cols.pkl'))

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/analysis.html')
def analysis():
    return app.send_static_file('analysis.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        ph = float(data.get('ph'))
        selected_chemicals = data.get('chemicals', []) # Expecting a list

        # Prepare feature row
        # feature_cols = ['ph', 'Lead', 'Mercury', 'Arsenic', 'Fluoride', 'Pesticides', 'Bacteria']
        input_data = {'ph': ph}
        for col in feature_cols:
            if col != 'ph':
                input_data[col] = 1 if col in selected_chemicals else 0

        X = pd.DataFrame([input_data], columns=feature_cols)

        # Predict
        treatment = model_treatment.predict(X)[0]
        disease = model_disease.predict(X)[0]

        return jsonify({
            'success': True,
            'treatment': treatment,
            'disease': disease
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
