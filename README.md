# 💬 Hate Speech Classification (Logistic Regression)

A simple Flask-based web application and API for classifying hate speech using a Logistic Regression model trained on TF-IDF features.

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements/local.txt
````


## 🧠 Training the Model

To train the model on the preprocessed dataset:

```bash
python3 train.py
```

This will generate a `pipeline.joblib` file that includes both the TF-IDF vectorizer and the trained classifier.

---

## 🔍 Running Predictions

Once the model is trained, you can test it using command below the write speech and enter:

```bash
python3 predict.py
```

You will get a response like:

```
Positive (non-hate) (0.95 confidence)
```

---

## 🌐 Web App & API (Render Ready)

You can run the Flask app locally:

```bash
python app.py
```

The app provides:

* ✅ A simple web form
* ✅ A live prediction result
* ✅ A dynamic API link preview
* ✅ A public JSON API endpoint

---

## 🔗 API Usage

### GET

```http
GET /api/predict?text=I love you
```

### POST

```http
POST /api/predict
Content-Type: application/json

{
  "text": "I hate you"
}
```


4. Live URL link:

```
https://hate-speech-classifier.onrender.com
```


## 🧼 License

MIT License © helinatefera
