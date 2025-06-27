from .hate_speech import HateSpeechDataset
from scripts.preprocess import preprocess_text

dataset = HateSpeechDataset().download().load()
df = dataset.get_dataframe()
df = df.dropna(subset=["Content", "Label"])
df["Content"] = df["Content"].astype(str).apply(preprocess_text)
df = df.dropna(subset=["Content", "Label"])
print(f"Dataset loaded with {len(df)} entries.")