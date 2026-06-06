from src.utils.device import check_vram_requirements
from src.routing.model_registry import ModelRegistry
from src.routing.config_manager import ConfigManager
import importlib

class ModalityRouter:
    """
    Routes generation requests to the correct model pipeline and 
    enforces VRAM limits for the RTX 4050 target.
    """
    REGISTRY = {
        "xray": {
            "backbone": "stabilityai/stable-diffusion-2-1",
            "adapter":  "xray_lora.pt",
            "vram_gb":  3.8,
            "pipeline_module": "src.generation.xray.pipeline",
            "pipeline_class": "XrayGenerationPipeline"
        },
        "ct": {
            "backbone": "MONAI/generative_ct",
            "adapter":  "ct_lora.pt",
            "vram_gb":  4.5,
            "pipeline_module": "src.generation.ct.pipeline",
            "pipeline_class": "CTGenerationPipeline"
        },
        "mri": {
            "backbone": "SynthSeg/label_to_image_v2",
            "adapter":  "mri_lora.pt",
            "vram_gb":  2.0,
            "pipeline_module": "src.generation.mri.pipeline",
            "pipeline_class": "MRIGenerationPipeline"
        },
        "ultrasound": {
            "backbone": "stabilityai/stable-diffusion-2-1",
            "adapter":  "ultrasound_lora.pt",
            "vram_gb":  3.5,
            "pipeline_module": "src.generation.ultrasound.pipeline",
            "pipeline_class": "UltrasoundGenerationPipeline"
        },
        "mammography": {
            "backbone": "stabilityai/stable-diffusion-2-1",
            "adapter":  "mammography_lora.pt",
            "vram_gb":  4.8,
            "pipeline_module": "src.generation.mammography.pipeline",
            "pipeline_class": "MammographyGenerationPipeline"
        },
        "cardiac_mri": {
            "backbone": "MONAI/generative_cardiac",
            "adapter":  "cardiac_lora.pt",
            "vram_gb":  4.2,
            "pipeline_module": "src.generation.cardiac_mri.pipeline",
            "pipeline_class": "CardiacMRIGenerationPipeline"
        },
        "pet_ct": {
            "backbone": "MONAI/generative_ct",
            "adapter":  "pet_ct_lora.pt",
            "vram_gb":  4.5,
            "pipeline_module": "src.generation.pet_ct.pipeline",
            "pipeline_class": "PETCTGenerationPipeline"
        },
        "inpainting": {
            "backbone": "stabilityai/stable-diffusion-2-inpainting",
            "adapter":  "inpainting_lora.pt",
            "vram_gb":  4.0,
            "pipeline_module": "src.generation.inpainting.pipeline",
            "pipeline_class": "InpaintingPipeline"
        }
    }

    def __init__(self):
        self.registry = ModelRegistry()
        self.config_manager = ConfigManager()

    def get_pipeline(self, modality, device="cuda"):
        if modality not in self.REGISTRY:
            raise ValueError(f"Unsupported modality: {modality}")
            
        cfg = self.REGISTRY[modality]
        
        # 1. Enforce RTX 4050 6GB VRAM constraint before loading
        check_vram_requirements(cfg["vram_gb"])
        
        # 2. Lazy load the pipeline class to avoid circular dependencies
        try:
            module = importlib.import_module(cfg["pipeline_module"])
            PipelineClass = getattr(module, cfg["pipeline_class"])
        except ImportError:
            raise NotImplementedError(f"Pipeline for {modality} is not fully implemented yet.")
            
        # 3. Instantiate pipeline structure
        pipeline = PipelineClass(backbone=cfg["backbone"])
        
        # 4. Load LoRA adapter if it exists in the adapters/ dir
        exists, adapter_path = self.registry.check_adapter_exists(cfg["adapter"])
        if exists:
            pipeline.load_adapter(str(adapter_path))
        else:
            print(f"Warning: Adapter {cfg['adapter']} not found. Running base backbone only.")
            
        return pipeline.to(device)
