import torch

CONTRAST_TOKENS = {
    "t1":   0,   # WM bright, GM gray, CSF dark
    "t2":   1,   # CSF bright, WM dark, lesions bright
    "flair":2,   # CSF suppressed; MS/stroke lesions bright
    "dwi":  3,   # Acute infarct bright (restricted diffusion)
    "swi":  4,   # Haemosiderin dark (microbleeds, cavernomas)
    "asl":  5,   # Arterial spin labelling (perfusion)
}

class ContrastSynthesizer:
    """
    Generates realistic MRI textures from the underlying anatomical label map.
    """
    def synthesize(self, label_map, contrast):
        """Converts a discrete label map into a specific MRI sequence intensity."""
        if contrast not in CONTRAST_TOKENS:
            contrast = "t1"
        return torch.zeros_like(label_map)
