from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    
    if user_message.strip().lower() == "hi":
        response = "Hello"
    else:
        response = "I don't understand."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
