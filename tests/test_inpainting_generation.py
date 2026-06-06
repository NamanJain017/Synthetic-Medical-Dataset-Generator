from src.generation.inpainting.pipeline import InpaintingPipeline

def test_inpaint_pipeline_init():
    pipeline = InpaintingPipeline(device="cpu")
    assert pipeline is not None
