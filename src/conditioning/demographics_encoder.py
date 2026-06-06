import torch
import torch.nn as nn
import torch.nn.functional as F

class DemographicsEncoder(nn.Module):
    """
    Encodes continuous age and categorical sex into a dense representation.
    """
    def __init__(self, embed_dim=128):
        super().__init__()
        self.age_proj = nn.Linear(1, embed_dim//2)    # Age norm [0,1]
        self.sex_emb  = nn.Embedding(3, embed_dim//2) # M/F/unspecified
        self.proj = nn.Linear((embed_dim//2) * 2, embed_dim)

    def forward(self, age_norm, sex_token):
        """
        age_norm: Tensor of shape (B,) with normalized age values in [0,1]
        sex_token: Tensor of shape (B,) with integer tokens (0=M, 1=F, 2=unspecified)
        """
        age_emb = F.relu(self.age_proj(age_norm.unsqueeze(-1)))
        sex_emb = self.sex_emb(sex_token)
        return self.proj(torch.cat([age_emb, sex_emb], dim=-1))
