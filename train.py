import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import random
import numpy as np
from datasets.load_dataset import load_clean_dataset

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

# Prepare input and target
data = load_clean_dataset()
X = data["Content"].astype(str)
y = data["Label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

vectorizer = TfidfVectorizer(
    stop_words="english",
    lowercase=True,
    ngram_range=(1, 2),
    max_features=10000,
    min_df=3,
    max_df=0.9,
)

model = LogisticRegression(
    penalty="l2", C=1.0, solver="liblinear", max_iter=500, verbose=1,random_state=SEED
)

pipeline = make_pipeline(vectorizer, model)
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "pipeline.joblib")
