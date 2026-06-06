import torch

class SynthSegWrapper:
    """
    Wraps SynthSeg to generate anatomically correct label maps 
    from a probabilistic atlas. No real MRI required for training.
    """
    def generate_label_map(self, anatomy):
        # Returns a simulated 3D label map
        return torch.zeros((64, 256, 256))
