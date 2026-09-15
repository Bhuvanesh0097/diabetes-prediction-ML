
import os
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "diabetes_logistic_regression_model.joblib"

model = joblib.load(MODEL_PATH)

# Features used during model training
FEATURES = [
    "gender",
    "age",
    "hypertension",
    "heart_disease",
    "smoking_history",
    "bmi",
    "HbA1c_level",
    "blood_glucose_level"
]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read JSON input
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "status": "error",
                "message": "Request body must contain valid JSON."
            }), 400

        # Check that all required features are present
        missing_features = [
            feature for feature in FEATURES
            if feature not in data
        ]

        if missing_features:
            return jsonify({
                "status": "error",
                "message": "Missing features",
                "missing_features": missing_features
            }), 400

        # Create DataFrame in the same feature order as training
        input_df = pd.DataFrame(
            [[data[feature] for feature in FEATURES]],
            columns=FEATURES
        )

        # Generate prediction
        prediction = int(model.predict(input_df)[0])

        # Generate probability
        probability = float(
            model.predict_proba(input_df)[0][1]
        )

        # Return result
        return jsonify({
            "status": "success",
            "prediction": prediction,
            "diabetes_probability": round(probability, 4),
            "message": (
                "Diabetic" if prediction == 1
                else "Non-diabetic"
            )
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
