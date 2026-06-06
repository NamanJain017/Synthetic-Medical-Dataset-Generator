import numpy as np

def normalize_image(image, modality, **kwargs):
    """
    Provides unified access to modality-specific normalizations.
    Ensures all generation modules receive data in [0, 1] range.
    """
    if modality == "xray" or modality == "mammography":
        if image.max() > 1.0:
            return image / 255.0
        return image
        
    elif modality == "mri":
        # MRI typically uses Z-score normalization rather than strict [0,1]
        # But for diffusion models, it's often min-maxed after Z-score
        mu = image[image > 0].mean()
        std = image[image > 0].std()
        z_scored = (image - mu) / (std + 1e-8)
        
        # Min-max scale the Z-scored image to [0,1] for diffusion
        z_min, z_max = z_scored.min(), z_scored.max()
        return (z_scored - z_min) / (z_max - z_min + 1e-8)
        
    elif modality == "ct":
        # CT is normalized via MONAI's ScaleIntensityRanged using HU windows
        # If it hits this function, it should already be [0,1] or we fallback
        img_min = image.min()
        img_max = image.max()
        if img_max == img_min: return image
        return (image - img_min) / (img_max - img_min)
        
    elif modality == "ultrasound":
        # Usually log compressed. Fallback to min-max
        img_min = image.min()
        img_max = image.max()
        if img_max == img_min: return image
        return (image - img_min) / (img_max - img_min)
        
    else:
        # Default fallback min-max
        img_min = image.min()
        img_max = image.max()
        if img_max == img_min: return image
        return (image - img_min) / (img_max - img_min)
