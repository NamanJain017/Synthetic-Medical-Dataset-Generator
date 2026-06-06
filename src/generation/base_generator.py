import torch
import torch.nn as nn

class BaseGeneratorPipeline:
    """
    Abstract base class for all modality generation pipelines.
    Handles device placement and PEFT LoRA adapter loading.
    """
    def __init__(self, backbone, device="cuda"):
        self.device = device
        self.backbone = backbone
        self.model = None

    def load_adapter(self, adapter_path):
        """
        Loads LoRA weights via PEFT.
        """
        if self.model is not None:
            try:
                from peft import PeftModel
                self.model = PeftModel.from_pretrained(self.model, adapter_path)
                self.model.to(self.device)
            except ImportError:
                print("Warning: peft library not installed. Cannot load LoRA adapter.")

    def to(self, device):
        self.device = device
        if self.model is not None:
            self.model.to(device)
        return self

    def generate(self, **kwargs):
        """
        Core generation function to be implemented by modality subclasses.
        """
        raise NotImplementedError("Subclasses must implement generate()")
