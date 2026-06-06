from ..base_generator import BaseGeneratorPipeline
from .calcification_injector import CalcificationInjector
from .view_conditioner import apply_view_conditioning
from .prompt_builder import build_mammography_prompt
import torch

class MammographyGenerationPipeline(BaseGeneratorPipeline):
    def __init__(self, backbone="stabilityai/stable-diffusion-2-1", device="cuda"):
        super().__init__(backbone, device)
        self.calc_injector = CalcificationInjector()
        self.model = None

    def generate(self, anatomy, disease, severity, view="mlo", birads=1, **kwargs):
        """
        Generates Mammograms with specific views and density/BIRADS conditioning.
        """
        prompt = build_mammography_prompt(disease, view, birads)
        
        # 1. Base generation logic
        base_img = torch.zeros((1, 512, 512))
        
        # 2. Inject calcifications if disease necessitates them
        base_img = self.calc_injector.inject(base_img, disease, severity)
        
        # 3. Apply view-specific spatial constraints
        base_img = apply_view_conditioning(base_img, view)
        
        return base_img
