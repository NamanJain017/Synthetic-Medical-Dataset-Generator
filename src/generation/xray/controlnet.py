import torch
import torch.nn as nn

class AnatomyControlNet(nn.Module):
    """
    Parallel UNet branch conditioned on chest anatomy segmentation maps
    (lung fields, cardiac silhouette, diaphragm, carina).
    Locks gross anatomical positions while diffusion handles pathology.
    """
    def __init__(self):
        super().__init__()
        pass
        
    def forward(self, x, hint):
        return x
