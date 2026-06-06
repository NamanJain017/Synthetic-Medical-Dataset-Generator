import os
from pathlib import Path

class ModelRegistry:
    """
    Manages local paths for base backbones and LoRA adapters.
    Ensures that required weights are available before routing.
    """
    def __init__(self, adapters_dir="adapters"):
        self.adapters_dir = Path(adapters_dir)
        # Create directory if it doesn't exist
        self.adapters_dir.mkdir(parents=True, exist_ok=True)

    def check_adapter_exists(self, adapter_name):
        """
        Returns a tuple: (boolean_exists, pathlib_path)
        """
        path = self.adapters_dir / adapter_name
        return path.exists(), path

    def get_huggingface_cache_dir(self):
        """
        Returns the HuggingFace cache directory where base models are stored.
        """
        return os.environ.get("HF_HOME", os.path.expanduser("~/.cache/huggingface"))
