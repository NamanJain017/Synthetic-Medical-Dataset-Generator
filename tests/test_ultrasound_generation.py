from src.generation.ultrasound.pipeline import UltrasoundGenerationPipeline

def test_us_pipeline_init():
    pipeline = UltrasoundGenerationPipeline(device="cpu")
    assert pipeline is not None
