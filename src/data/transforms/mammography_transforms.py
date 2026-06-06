import cv2
import numpy as np

def remove_pectoral(image, view="mlo"):
    """
    Removes pectoral muscle from MLO view using Hough lines/thresholding.
    Placeholder for geometric removal pipeline.
    """
    if view.lower() != "mlo":
        return image
    
    # In a full implementation, Hough line detection is used to isolate
    # the triangular pectoral muscle in the upper corner and mask it out.
    return image

def segment_breast(image):
    """
    Generates a binary mask of the breast tissue, excluding the air background.
    Useful for conditioning and QC.
    """
    if isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            # Scale to 0-255 for opencv thresholding if it's float
            img_scaled = (np.clip(image, 0, 1) * 255).astype(np.uint8)
        else:
            img_scaled = image
            
        _, binary = cv2.threshold(img_scaled, 10, 255, cv2.THRESH_BINARY)
        # Morphological closing to remove small holes
        return cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel=np.ones((20, 20), np.uint8))
    
    return image
