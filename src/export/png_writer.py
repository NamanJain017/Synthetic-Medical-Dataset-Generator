import cv2
import numpy as np

def write_png(image_tensor, output_path):
    """
    Exports simple 2D visualizations. Converts [0,1] float tensors to uint8 PNGs.
    """
    if hasattr(image_tensor, "numpy"):
        img = image_tensor.numpy()
    else:
        img = image_tensor
        
    if len(img.shape) == 3 and img.shape[0] in [1, 3]:
        img = np.transpose(img, (1, 2, 0))
        
    img_uint8 = (np.clip(img, 0, 1) * 255).astype(np.uint8)
    cv2.imwrite(output_path, img_uint8)
