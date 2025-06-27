import pandas as pd
import re
import string

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove user mentions and hashtags
    text = re.sub(r"[@#]\w+", "", text)

    # Remove numeric characters
    text = re.sub(r"\d+", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text