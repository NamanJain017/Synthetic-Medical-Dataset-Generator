import numpy as np

def rayleigh_speckle(image, sigma=0.3):
    """
    Correct speckle model for ultrasound.
    Rayleigh distribution arises from constructive/destructive
    interference of backscattered echoes. MUST be multiplicative.
    """
    noise = np.random.rayleigh(scale=sigma, size=image.shape)
    return np.clip(image * noise, 0, 1)   # Multiplicative, not additive
