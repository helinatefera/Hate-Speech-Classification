from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)
pipeline = joblib.load("app/pipeline.joblib")
classes = ["Positive (non-hate)", "Negative (hate)"]

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        prob = pipeline.predict_proba([text])[0]
        label = pipeline.predict([text])[0]
        prediction = classes[label]
        confidence = f"{max(prob):.2f}"

    return render_template("main.html", prediction=prediction, confidence=confidence, text=text)

@app.route("/api/predict", methods=["GET", "POST"])
def api_predict():
    if request.method == "POST":
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400
        text = data["text"]
    else:
        text = request.args.get("text")
        if not text:
            return jsonify({"error": "Missing 'text' query parameter"}), 400

    prob = pipeline.predict_proba([text])[0]
    label = pipeline.predict([text])[0]

    return jsonify({
        "text": text,
        "prediction": classes[label],
        "confidence": round(float(max(prob)), 4)
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
