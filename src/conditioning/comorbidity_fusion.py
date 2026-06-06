import torch
import torch.nn as nn

class ComorbidityFusion(nn.Module):
    """
    Fuses multiple concurrent diseases using multi-label conditioning.
    Each disease embedding is scaled by its severity, then summed.
    """
    def __init__(self, disease_ontology, severity_encoder):
        super().__init__()
        self.disease_ontology = disease_ontology
        self.severity_encoder = severity_encoder
        
    def forward(self, disease_severity_dict_list, device):
        """
        disease_severity_dict_list: List of dicts, 
        e.g., [{"lung_cancer":"moderate", "emphysema":"mild"}]
        """
        batch_embeddings = []
        
        for patient_dict in disease_severity_dict_list:
            patient_emb = None
            
            for disease, severity in patient_dict.items():
                d_emb = self.disease_ontology([disease], device)[0] # Shape: (embed_dim,)
                s_scalar = self.severity_encoder([severity], device, is_training=False)[0]
                
                scaled_d_emb = d_emb * s_scalar
                if patient_emb is None:
                    patient_emb = scaled_d_emb
                else:
                    patient_emb = patient_emb + scaled_d_emb
            
            # Fallback if empty dict
            if patient_emb is None:
                patient_emb = self.disease_ontology(["normal"], device)[0] * 0.0
                
            batch_embeddings.append(patient_emb)
            
        return torch.stack(batch_embeddings)
