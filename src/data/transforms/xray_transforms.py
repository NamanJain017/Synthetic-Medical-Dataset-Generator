from monai.transforms import (
    LoadImaged, 
    EnsureChannelFirstd, 
    Resized, 
    NormalizeIntensityd, 
    Compose
)
import cv2
import numpy as np

def apply_clahe(img_uint8):
    """
    Applies Contrast Limited Adaptive Histogram Equalization (CLAHE)
    to enhance X-ray bone and tissue contrast.
    """
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    return clahe.apply(img_uint8)

def get_xray_transforms(spatial_size=(512, 512)):
    """
    Returns the MONAI preprocessing pipeline for X-rays.
    """
    return Compose([
        LoadImaged(keys=["image"]),
        EnsureChannelFirstd(keys=["image"]),
        Resized(keys=["image"], spatial_size=spatial_size),
        NormalizeIntensityd(keys=["image"], nonzero=True, channel_wise=True),
    ])
