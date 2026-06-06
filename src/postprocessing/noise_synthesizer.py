import numpy as np

def add_quantum_mottle(image, dose_level="low"):
    """
    Simulates Poisson quantum noise seen in low-dose X-ray or CT.
    """
    factor = 10.0 if dose_level == "low" else 50.0
    
    # Scale image to simulating photon counts
    photon_counts = image * factor
    noisy = np.random.poisson(photon_counts) / factor
    
    return np.clip(noisy, 0, 1)
