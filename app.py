from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model, columns = joblib.load("model.pkl")

@app.route("/")
def home():
    return "ML API is running ✅"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Incoming data:", data)

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    prediction = model.predict(df)

    return jsonify({
        "predicted_score": round(prediction[0], 2)
    })

if __name__ == "__main__":
    app.run(debug=True)