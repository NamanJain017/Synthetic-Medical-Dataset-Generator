from ..base_generator import BaseGeneratorPipeline
from .speckle_model import rayleigh_speckle
from .prompt_builder import build_ultrasound_prompt
from .probe_geometry import apply_probe_mask
import torch
import numpy as np

class UltrasoundGenerationPipeline(BaseGeneratorPipeline):
    def __init__(self, backbone="stabilityai/stable-diffusion-2-1", device="cuda"):
        super().__init__(backbone, device)
        self.model = None
        
    def generate(self, anatomy, disease, severity, probe="curvilinear", **kwargs):
        """
        Generates Ultrasound images with correct Rayleigh speckle and probe geometry.
        """
        prompt = build_ultrasound_prompt(anatomy, disease, severity, probe)
        
        # 1. Base diffusion generation (placeholder)
        base_img = torch.zeros((1, 256, 256))
        
        # 2. Apply multiplicative Rayleigh speckle
        base_img_np = base_img.numpy()
        speckled = rayleigh_speckle(base_img_np, sigma=0.3)
        
        # 3. Apply probe geometry mask
        masked = apply_probe_mask(speckled, probe)
        
        return torch.from_numpy(masked)
