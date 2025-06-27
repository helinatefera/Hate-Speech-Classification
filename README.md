# 💬 Hate Speech Classification (Logistic Regression)

A simple Flask-based web application and API for classifying hate speech using a Logistic Regression model trained on TF-IDF features.

---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
````


## 🧠 Training the Model

To train the model on the preprocessed dataset:

```bash
python train.py
```

This will generate a `pipeline.joblib` file that includes both the TF-IDF vectorizer and the trained classifier.

---

## 🔍 Running Predictions

Once the model is trained, you can test it using:

```bash
python predict.py "I love everyone!"
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

Then open [http://localhost:5000](http://localhost:5000) in your browser.

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

---

## 🚀 Deploy to Render

1. Push this repo to GitHub
2. Create a new **Web Service** on [Render](https://render.com/)
3. Set **start command** to:

```bash
gunicorn app:app
```

4. That’s it. You’ll get a free live URL like:

```
https://hate-speech-classifier.onrender.com
```

---

## 📁 Project Structure

```
├── app.py               # Flask app
├── train.py             # Model training script
├── predict.py           # CLI predictor
├── pipeline.joblib      # Saved model pipeline
├── requirements.txt     # Dependencies
├── templates/
│   └── main.html        # UI template
```

---

## 🧼 License

MIT License © Your Name

```

Let me know if you want to replace `"Your Name"` with a real name or GitHub profile, or add badges/screenshots.
```
