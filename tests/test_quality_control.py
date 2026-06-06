from src.quality.qc_pipeline import QualityControlPipeline

def test_qc_pipeline_init():
    qc = QualityControlPipeline()
    assert qc is not None
