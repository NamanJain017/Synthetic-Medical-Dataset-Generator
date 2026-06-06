import json
import torch
import torch.nn as nn
from pathlib import Path

class DiseaseOntology(nn.Module):
    """
    Maps disease names -> structured radiological feature descriptors using SNOMED-CT.
    """
    def __init__(self, asset_path=None, embed_dim=256):
        super().__init__()
        if asset_path is None:
            # Default relative path from this file
            base_dir = Path(__file__).parent
            asset_path = base_dir / "assets" / "disease_map.json"
            
        with open(asset_path, "r") as f:
            self.disease_map = json.load(f)
            
        # Create a vocabulary of known diseases
        self.disease_vocab = list(self.disease_map.keys())
        self.disease_vocab.append("normal")
        self.disease_to_idx = {d: i for i, d in enumerate(self.disease_vocab)}
        
        # Simple lookup embedding table for disease
        self.embedding = nn.Embedding(len(self.disease_vocab), embed_dim)
        
    def get_features(self, disease_name):
        return self.disease_map.get(disease_name, {})
        
    def forward(self, disease_names, device):
        indices = []
        for d in disease_names:
            indices.append(self.disease_to_idx.get(d, self.disease_to_idx["normal"]))
        
        idx_tensor = torch.tensor(indices, dtype=torch.long, device=device)
        return self.embedding(idx_tensor)
