from src.generation.mri.pipeline import MRIGenerationPipeline

def test_mri_pipeline_init():
    pipeline = MRIGenerationPipeline(device="cpu")
    assert pipeline is not None
