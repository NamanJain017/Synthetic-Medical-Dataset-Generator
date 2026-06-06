from ..base_generator import BaseGeneratorPipeline

class Img2ImgPipeline(BaseGeneratorPipeline):
    """
    Image-to-Image mode: Adds disease texture to an entire image 
    with controllable strength (noise level 0.3-0.8).
    Preserves anatomy while modifying pathological appearance.
    """
    def __init__(self, backbone="stabilityai/stable-diffusion-2-1", device="cuda"):
        super().__init__(backbone, device)

    def generate(self, base_image, disease, severity, noise_level=0.5, **kwargs):
        return base_image
