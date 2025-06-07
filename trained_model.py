# trained_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neural_network import MLPClassifier
import joblib
import os

# 📁 Ensure the trained_data folder exists
os.makedirs("trained_data", exist_ok=True)

# 📥 Load dataset
df = pd.read_csv('csv/Students_Grading_Dataset.csv')

# ✅ Create Pass/Fail column using a rule
def pass_fail_logic(row):
    if (row['Attendance (%)'] >= 75 and
        row['Participation_Score'] >= 5 and
        row['Study_Hours_per_Week'] >= 7):
        return 'Pass'
    else:
        return 'Fail'

df['PassFail'] = df.apply(pass_fail_logic, axis=1)

# ✅ Features and target
X = df[['Attendance (%)', 'Participation_Score', 'Study_Hours_per_Week', 'Sleep_Hours_per_Night']]
y = df['PassFail']

# ✅ Encode target (Pass/Fail) to 0/1
y = y.map({'Fail': 0, 'Pass': 1})

# 📊 Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🧠 Pipeline: scale + MLP
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', MLPClassifier(
        hidden_layer_sizes=(32,),
        activation='relu',
        max_iter=1000,
        early_stopping=True,
        random_state=42
    ))
])

# 🏋️ Train
pipeline.fit(X_train, y_train)

# 💾 Save model
joblib.dump(pipeline, 'trained_data/student_pass_model.pkl')

print("✅ Model training complete. Saved to 'trained_data/student_pass_model.pkl'")
