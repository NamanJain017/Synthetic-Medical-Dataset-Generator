import torch
import torch.nn as nn
import random

class SeverityEncoder(nn.Module):
    """
    Encodes severity levels into a scalar multiplier.
    Supports random dropout for Classifier-Free Guidance (CFG).
    """
    SCALARS = {
        "mild": 0.25,
        "moderate": 0.55,
        "severe": 0.90,
        "normal": 0.0
    }
    
    def __init__(self, p_dropout=0.10):
        super().__init__()
        self.p_dropout = p_dropout
        
    def forward(self, severities, device, is_training=False):
        batch_scalars = []
        for s in severities:
            if is_training and random.random() < self.p_dropout:
                batch_scalars.append(0.0)  # CFG Dropout
            else:
                batch_scalars.append(self.SCALARS.get(s, 0.55)) # Default moderate
                
        return torch.tensor(batch_scalars, dtype=torch.float32, device=device)
