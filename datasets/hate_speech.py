import os
import shutil

import kagglehub
import pandas as pd


class HateSpeechDataset:
    def __init__(self, target_dir="data"):
        self.dataset_id = (
            "waalbannyantudre/hate-speech-detection-curated-dataset"
        )
        self.filename = "HateSpeechDatasetBalanced.csv"
        self.target_dir = target_dir
        self.local_path = os.path.join(target_dir, self.filename)
        os.makedirs(self.target_dir, exist_ok=True)

    def download(self):
        if os.path.exists(self.local_path):
            print("Dataset already exists at", self.local_path)
            return self
        raw_path = kagglehub.dataset_download(self.dataset_id)
        source_file = os.path.join(raw_path, self.filename)
        shutil.copy2(source_file, self.local_path)
        return self

    def load(self):
        self.df = pd.read_csv(self.local_path)
        return self

    def get_dataframe(self):
        if not hasattr(self, "df"):
            raise ValueError(
                "Dataset not loaded. Call download().load() first."
            )
        return self.df
