from src.generation.mammography.pipeline import MammographyGenerationPipeline

def test_mammo_pipeline_init():
    pipeline = MammographyGenerationPipeline(device="cpu")
    assert pipeline is not None
