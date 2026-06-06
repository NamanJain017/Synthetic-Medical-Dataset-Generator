import torch
import torch.nn as nn

class AnatomyEncoder(nn.Module):
    """
    Encodes body part, imaging plane, and laterality into a dense conditioning vector.
    """
    BODY_PARTS = ["chest","brain","abdomen","spine","breast",
                  "cardiac","msk","pelvis","neck","vascular"]
    PLANES     = ["axial","coronal","sagittal","pa","ap","lateral",
                  "cc","mlo"]       # last two for mammography
    LATERALITY = ["left","right","bilateral","na"]

    def __init__(self, embed_dim=128):
        super().__init__()
        self.part_emb  = nn.Embedding(len(self.BODY_PARTS), embed_dim//3)
        self.plane_emb = nn.Embedding(len(self.PLANES),     embed_dim//3)
        self.lat_emb   = nn.Embedding(len(self.LATERALITY), embed_dim//3)
        
        # Account for any remainder in division
        cat_dim = (embed_dim//3) * 3
        self.proj = nn.Linear(cat_dim, embed_dim)

        self.part_to_idx = {p: i for i, p in enumerate(self.BODY_PARTS)}
        self.plane_to_idx = {p: i for i, p in enumerate(self.PLANES)}
        self.lat_to_idx = {p: i for i, p in enumerate(self.LATERALITY)}

    def forward(self, parts, planes, lateralities, device):
        p_idx = torch.tensor([self.part_to_idx.get(p, 0) for p in parts], device=device)
        pl_idx = torch.tensor([self.plane_to_idx.get(p, 0) for p in planes], device=device)
        l_idx = torch.tensor([self.lat_to_idx.get(l, 0) for l in lateralities], device=device)

        p_e = self.part_emb(p_idx)
        pl_e = self.plane_emb(pl_idx)
        l_e = self.lat_emb(l_idx)
        
        return self.proj(torch.cat([p_e, pl_e, l_e], dim=-1))
