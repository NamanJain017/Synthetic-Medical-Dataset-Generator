from src.generation.ct.pipeline import CTGenerationPipeline

def test_ct_pipeline_init():
    pipeline = CTGenerationPipeline(device="cpu")
    assert pipeline is not None
