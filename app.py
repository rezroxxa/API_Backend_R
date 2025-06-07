from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 Enables cross-origin requests
import joblib
import pandas as pd

app = Flask(__name__)  # 👈 Use __name__, not name
CORS(app)  # 👈 Enable CORS for all routes

# Load model
model = joblib.load('trained_data/student_pass_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

    # Predict
    result = model.predict(input_df)[0]
    prediction = 'Pass' if result == 1 else 'Fail'

    return jsonify({'prediction': prediction})

if __name__ == '__main__':  # 👈 Fix this too
    app.run(debug=True)
