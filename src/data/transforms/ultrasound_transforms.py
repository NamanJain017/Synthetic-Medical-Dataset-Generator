import numpy as np

def log_compress(image, dynamic_range_db=60):
    """
    Simulates scanner log-compression of RF envelope data
    for ultrasound image formation.
    """
    eps = 1e-10
    compressed = 20 * np.log10(image + eps)
    compressed = np.clip(compressed, -dynamic_range_db, 0)
    return (compressed + dynamic_range_db) / dynamic_range_db

def apply_tgc(image, depth_axis=0):
    """
    Time Gain Compensation (TGC) — corrects for acoustic attenuation with depth.
    """
    n_rows = image.shape[depth_axis]
    tgc_curve = np.linspace(1.0, 2.5, n_rows)
    
    if depth_axis == 0:
        return image * tgc_curve.reshape(-1, 1)
    elif len(image.shape) > 1:
        return image * tgc_curve.reshape(1, -1)
    else:
        return image * tgc_curve
