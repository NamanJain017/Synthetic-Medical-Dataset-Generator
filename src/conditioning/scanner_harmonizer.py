import torch
import torch.nn as nn
import json
from pathlib import Path

class ScannerHarmonizer(nn.Module):
    """
    Scanner vendor style conditioning to simulate differences
    between GE, Siemens, Philips, etc.
    """
    def __init__(self, embed_dim=128, asset_path=None):
        super().__init__()
        if asset_path is None:
            base_dir = Path(__file__).parent
            asset_path = base_dir / "assets" / "scanner_profiles.json"
            
        with open(asset_path, "r") as f:
            data = json.load(f)
            self.scanner_tokens = data.get("tokens", {})
            
        self.scanner_emb = nn.Embedding(len(self.scanner_tokens) + 1, embed_dim)
        self.default_token = self.scanner_tokens.get("generic", 6)
        
    def forward(self, scanners, device):
        idx_list = [self.scanner_tokens.get(s, self.default_token) for s in scanners]
        idx_tensor = torch.tensor(idx_list, dtype=torch.long, device=device)
        return self.scanner_emb(idx_tensor)
