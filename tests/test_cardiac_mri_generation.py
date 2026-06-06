from src.generation.cardiac_mri.pipeline import CardiacMRIGenerationPipeline

def test_cardiac_pipeline_init():
    pipeline = CardiacMRIGenerationPipeline(device="cpu")
    assert pipeline is not None
