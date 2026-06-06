from src.generation.xray.pipeline import XrayGenerationPipeline

def test_xray_pipeline_init():
    pipeline = XrayGenerationPipeline(device="cpu")
    assert pipeline is not None
