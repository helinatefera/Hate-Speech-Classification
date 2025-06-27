import joblib

pipeline = joblib.load("pipeline.joblib")
text = input("Enter text: ")
prob = pipeline.predict_proba([text])[0]
label = pipeline.predict([text])[0]
classes = ["non-hate", "hate"]
print(f"{classes[label]} ({max(prob):.2f} confidence)")