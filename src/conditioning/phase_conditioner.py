import torch
import torch.nn as nn

class PhaseConditioner(nn.Module):
    """
    Encodes CT timing phases (e.g., arterial, venous, delayed).
    """
    PHASES = [
        "non_contrast", 
        "arterial", 
        "portal_venous", 
        "delayed", 
        "corticomedullary",
        "na"
    ]
    
    def __init__(self, embed_dim=128):
        super().__init__()
        self.phase_emb = nn.Embedding(len(self.PHASES), embed_dim)
        self.phase_to_idx = {p: i for i, p in enumerate(self.PHASES)}
        
    def forward(self, phases, device):
        idx_list = [self.phase_to_idx.get(p, self.phase_to_idx["na"]) for p in phases]
        idx_tensor = torch.tensor(idx_list, dtype=torch.long, device=device)
        return self.phase_emb(idx_tensor)
