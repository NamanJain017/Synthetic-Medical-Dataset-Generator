import torch
import torch.nn as nn

class ConditioningFusion(nn.Module):
    """
    Final fusion module that concatenates all active conditioning 
    embeddings and projects them to the UNet cross-attention dimension.
    """
    def __init__(self, input_dim, cross_attention_dim=768):
        super().__init__()
        self.proj = nn.Linear(input_dim, cross_attention_dim)
        
    def forward(self, disease_emb, anatomy_emb, severity, modality_tok,
                demographics_emb=None, phase_tok=None, scanner_tok=None):
        
        # severity is expected to be shape (B,) so we add an unsqueeze
        parts = [disease_emb, anatomy_emb, severity.unsqueeze(-1), modality_tok]
        
        if demographics_emb is not None: 
            parts.append(demographics_emb)
        if phase_tok is not None:        
            parts.append(phase_tok)
        if scanner_tok is not None:      
            parts.append(scanner_tok)
            
        concat = torch.cat(parts, dim=-1)
        return self.proj(concat)
