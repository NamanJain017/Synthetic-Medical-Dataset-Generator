import yaml
from pathlib import Path

class ConfigManager:
    """
    Loads and merges modality-specific generation parameters from YAML configs.
    """
    def __init__(self, config_dir="configs"):
        self.config_dir = Path(config_dir)
        self.default_config = self._load_yaml("default.yaml")

    def _load_yaml(self, filename):
        path = self.config_dir / filename
        if not path.exists():
            return {}
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def get_config(self, modality):
        """
        Returns merged configuration for the requested modality.
        Combines global defaults with modality-specific overrides.
        """
        modality_cfg = self._load_yaml(f"{modality}_generation.yaml")
        
        # Merge dictionaries (modality specific overrides defaults)
        merged = {**self.default_config}
        merged.update(modality_cfg)
        
        return merged
