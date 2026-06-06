import torch
import torch.nn.functional as F

def upscale_image(image_tensor, scale_factor=2, mode='bicubic'):
    """
    Upscales the generated image (e.g. from 512 to 1024).
    In a full implementation, this might use a Real-ESRGAN or Latent Upscaler.
    For this scaffolding, we use standard interpolation.
    """
    if len(image_tensor.shape) == 3:
        image_tensor = image_tensor.unsqueeze(0)
    
    return F.interpolate(image_tensor, scale_factor=scale_factor, mode=mode, align_corners=False)
