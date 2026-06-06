from ..base_generator import BaseGeneratorPipeline
from .synthseg_wrapper import SynthSegWrapper
from .lesion_injector import LesionInjector
from .contrast_synthesis import ContrastSynthesizer
import torch

class MRIGenerationPipeline(BaseGeneratorPipeline):
    def __init__(self, backbone="SynthSeg/label_to_image_v2", device="cuda"):
        super().__init__(backbone, device)
        self.synthseg = SynthSegWrapper()
        self.injector = LesionInjector()
        self.synthesizer = ContrastSynthesizer()
        
    def generate(self, anatomy, disease, severity, contrast="t1", **kwargs):
        """
        Generates an MRI volume via label-map synthesis and contrast transformation.
        """
        # 1. Generate label map
        label_map = self.synthseg.generate_label_map(anatomy)
        # 2. Inject lesion into label map
        label_map = self.injector.inject(label_map, disease, severity)
        # 3. Synthesize specific contrast
        return self.synthesizer.synthesize(label_map, contrast)
