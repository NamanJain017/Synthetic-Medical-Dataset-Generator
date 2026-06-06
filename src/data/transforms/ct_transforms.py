from monai.transforms import (
    LoadImaged, 
    EnsureChannelFirstd, 
    Spacingd, 
    ScaleIntensityRanged, 
    CropForegroundd, 
    ToTensord, 
    Compose
)

# HU window presets for specific anatomies
WINDOWS = {
    "lung":        {"a_min": -1350, "a_max": 150},   # W:1500 L:-600
    "soft_tissue": {"a_min": -135,  "a_max": 215},   # W:350  L:40
    "brain":       {"a_min": 0,     "a_max": 80},    # W:80   L:40
    "bone":        {"a_min": -500,  "a_max": 1500},  # W:2000 L:500
    "liver":       {"a_min": -25,   "a_max": 230},   # W:255  L:100
}

def get_ct_transforms(window="lung"):
    """
    Returns the MONAI preprocessing pipeline for CT volumes
    with specific Hounsfield Unit windowing.
    """
    win = WINDOWS.get(window, WINDOWS["lung"])
    
    return Compose([
        LoadImaged(keys=["image", "label"], allow_missing_keys=True),
        EnsureChannelFirstd(keys=["image", "label"], allow_missing_keys=True),
        Spacingd(keys=["image", "label"], pixdim=(1.5, 1.5, 2.0), allow_missing_keys=True),
        ScaleIntensityRanged(
            keys=["image"],
            a_min=win["a_min"], 
            a_max=win["a_max"],
            b_min=0.0, 
            b_max=1.0, 
            clip=True
        ),
        CropForegroundd(keys=["image", "label"], source_key="image", allow_missing_keys=True),
        ToTensord(keys=["image", "label"], allow_missing_keys=True),
    ])
