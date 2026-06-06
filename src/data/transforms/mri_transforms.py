import SimpleITK as sitk
import numpy as np

def n4_bias_correction(image_path):
    """
    Applies N4 Bias Field Correction to an MRI image to fix 
    low-frequency intensity non-uniformity.
    """
    image = sitk.ReadImage(image_path, sitk.sitkFloat32)
    mask  = sitk.OtsuThreshold(image, 0, 1, 200)
    corrector = sitk.N4BiasFieldCorrectionImageFilter()
    corrector.SetMaximumNumberOfIterations([50, 50, 50, 50])
    return corrector.Execute(image, mask)

def zscore_normalize(volume):
    """
    Standard Z-score normalization for MRI volumes (ignoring background).
    """
    if isinstance(volume, sitk.Image):
        volume = sitk.GetArrayFromImage(volume)
        
    mu  = volume[volume > 0].mean()
    std = volume[volume > 0].std()
    return (volume - mu) / (std + 1e-8)
