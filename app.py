# app.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

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

    return jsonify({
        'prediction': prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
