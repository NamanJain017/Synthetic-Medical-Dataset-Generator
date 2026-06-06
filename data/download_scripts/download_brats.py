import os

def download_brats(target_dir="data/raw/brats"):
    """
    Downloads BraTS (Brain Tumor Segmentation) Dataset.
    Requires Synapse account and agreement to terms.
    """
    os.makedirs(target_dir, exist_ok=True)
    print(f"Please download BraTS from Synapse: https://www.synapse.org/#!Synapse:syn51156910/wiki/622351")
    print(f"Extract contents to {target_dir}")

if __name__ == "__main__":
    download_brats()
