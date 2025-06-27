from scripts.preprocess import preprocess_text

from .hate_speech import HateSpeechDataset


def load_clean_dataset():
    dataset = HateSpeechDataset().download().load()
    df = dataset.get_dataframe()
    df = df.dropna(subset=["Content", "Label"])
    df["Content"] = df["Content"].astype(str).apply(preprocess_text)
    df = df.dropna(subset=["Content", "Label"])
    print(f"Dataset loaded with {len(df)} entries.")
    return df


# load_clean_dataset()
