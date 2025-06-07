<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 Enables cross-origin requests
import joblib
import pandas as pd

app = Flask(__name__)  # 👈 Use __name__, not name
CORS(app)  # 👈 Enable CORS for all routes
=======
# app.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
>>>>>>> 8fdb801f28ced5b7d61b65d233b967520c0f1b2e

# Load model
model = joblib.load('trained_data/student_pass_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
<<<<<<< HEAD

    # Convert to DataFrame
    input_df = pd.DataFrame([data])

=======
    
    # Convert to DataFrame
    input_df = pd.DataFrame([data])
    
>>>>>>> 8fdb801f28ced5b7d61b65d233b967520c0f1b2e
    # Predict
    result = model.predict(input_df)[0]
    prediction = 'Pass' if result == 1 else 'Fail'

<<<<<<< HEAD
    return jsonify({'prediction': prediction})

if __name__ == '__main__':  # 👈 Fix this too
=======
    return jsonify({
        'prediction': prediction
    })

if __name__ == '__main__':
>>>>>>> 8fdb801f28ced5b7d61b65d233b967520c0f1b2e
    app.run(debug=True)
