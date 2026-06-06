import numpy as np
import cv2

def add_motion_blur(image, kernel_size=15, angle=0):
    """
    Simulates patient motion during acquisition.
    Common in X-ray and MRI.
    """
    if isinstance(image, np.ndarray):
        if image.dtype != np.float32 and image.dtype != np.float64:
            img_scaled = image.astype(np.float32)
        else:
            img_scaled = image
            
        kernel = np.zeros((kernel_size, kernel_size))
        kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size)
        kernel /= kernel_size
        
        # Rotate kernel by angle
        M = cv2.getRotationMatrix2D((kernel_size/2, kernel_size/2), angle, 1)
        kernel = cv2.warpAffine(kernel, M, (kernel_size, kernel_size))
        
        return cv2.filter2D(img_scaled, -1, kernel)
    return image

def add_beam_hardening(ct_slice):
    """
    Simulates dark streak artifacts between dense bones in CT.
    """
    # Placeholder for ray-tracing simulation of spectral shift
    return ct_slice
