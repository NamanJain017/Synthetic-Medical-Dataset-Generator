from ..base_generator import BaseGeneratorPipeline
from .temporal_diffusion import TemporalCineGenerator

class CardiacMRIGenerationPipeline(BaseGeneratorPipeline):
    def __init__(self, backbone="MONAI/generative_cardiac", device="cuda"):
        super().__init__(backbone, device)
        self.generator = TemporalCineGenerator()

    def generate(self, anatomy, disease, severity, **kwargs):
        """
        Generates a sequence of 2D images over time (cine) for Cardiac MRI.
        """
        return self.generator.generate_cine(disease, severity)
