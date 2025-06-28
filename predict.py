import joblib

pipeline = joblib.load("app/pipeline.joblib")
text = input("Enter text: ")
prob = pipeline.predict_proba([text])[0]
label = pipeline.predict([text])[0]
classes = ["Positive(non-hate)", "negative(hate)"]
print(f"{classes[label]} ({max(prob):.2f} confidence)")
