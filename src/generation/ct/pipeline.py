from ..base_generator import BaseGeneratorPipeline
from .autoregressive import AutoRegressiveCTGenerator
import torch

class CTGenerationPipeline(BaseGeneratorPipeline):
    def __init__(self, backbone="MONAI/generative_ct", device="cuda"):
        super().__init__(backbone, device)
        self.generator = AutoRegressiveCTGenerator()
        
    def generate(self, anatomy, disease, severity, phase="non_contrast", **kwargs):
        """
        Generates a 3D CT volume using 2.5D auto-regressive latent diffusion.
        """
        return self.generator.generate_volume(anatomy, disease, severity)
