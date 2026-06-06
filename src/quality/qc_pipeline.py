from .anatomy_validator import AnatomyValidator
from .pathology_verifier import PathologyVerifier
from .metrics import calculate_fid, calculate_ssim
from .heatmap_generator import HeatmapGenerator
from .radiomics_extractor import RadiomicsExtractor

class QualityControlPipeline:
    """
    Orchestrates the entire Quality Control gate.
    Generated images must pass this pipeline before being exported or
    used in downstream training sets.
    """
    def __init__(self):
        self.anatomy = AnatomyValidator()
        self.pathology = PathologyVerifier()
        self.heatmap = HeatmapGenerator()
        self.radiomics = RadiomicsExtractor()

    def run_qc(self, image_tensor, mask_tensor, anatomy, disease, severity):
        passed_anat, msg = self.anatomy.validate(image_tensor, anatomy)
        passed_path, conf = self.pathology.verify(image_tensor, disease, severity)
        
        status = "PASSED" if (passed_anat and passed_path) else "REJECTED"
        
        # Optional: Extract radiomics if mask is provided
        features = {}
        if mask_tensor is not None:
            features = self.radiomics.extract_features(image_tensor, mask_tensor)
            
        return {
            "status": status,
            "anatomy_valid": passed_anat,
            "pathology_confidence": conf,
            "anatomy_message": msg,
            "radiomic_features": features
        }
