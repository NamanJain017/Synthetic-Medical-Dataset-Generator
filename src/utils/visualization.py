import matplotlib.pyplot as plt
import numpy as np
import torch

def plot_2d_image(image_tensor, title="Image", cmap="gray"):
    """
    Plots a 2D image from a tensor or numpy array.
    """
    if isinstance(image_tensor, torch.Tensor):
        img = image_tensor.detach().cpu().numpy()
    else:
        img = image_tensor
        
    # Handle C, H, W to H, W, C
    if len(img.shape) == 3 and img.shape[0] in [1, 3]:
        img = np.transpose(img, (1, 2, 0))
    # Squeeze if single channel
    if len(img.shape) == 3 and img.shape[-1] == 1:
        img = img.squeeze(-1)

    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def plot_3d_volume(volume_tensor, slice_idx=None, axis=0, title="3D Volume", cmap="gray"):
    """
    Plots a 2D slice from a 3D volume (e.g., CT, MRI).
    axis 0: Axial, 1: Coronal, 2: Sagittal
    """
    if isinstance(volume_tensor, torch.Tensor):
        vol = volume_tensor.detach().cpu().numpy()
    else:
        vol = volume_tensor
        
    # Assume shape is (D, H, W) or (C, D, H, W)
    if len(vol.shape) == 4 and vol.shape[0] == 1:
        vol = vol.squeeze(0)
        
    if slice_idx is None:
        slice_idx = vol.shape[axis] // 2
        
    if axis == 0:
        slice_img = vol[slice_idx, :, :]
    elif axis == 1:
        slice_img = vol[:, slice_idx, :]
    else:
        slice_img = vol[:, :, slice_idx]
        
    plot_2d_image(slice_img, title=f"{title} (Axis={axis}, Slice={slice_idx})", cmap=cmap)

def create_collage(images, titles=None, cols=4, cmap="gray"):
    """
    Creates a grid collage of multiple 2D images.
    """
    n = len(images)
    rows = (n + cols - 1) // cols
    
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 4))
    axes = axes.flatten() if n > 1 else [axes]
    
    for i, img in enumerate(images):
        if isinstance(img, torch.Tensor):
            img = img.detach().cpu().numpy()
            
        if len(img.shape) == 3 and img.shape[0] in [1, 3]:
            img = np.transpose(img, (1, 2, 0))
        if len(img.shape) == 3 and img.shape[-1] == 1:
            img = img.squeeze(-1)
            
        axes[i].imshow(img, cmap=cmap)
        axes[i].axis("off")
        if titles and i < len(titles):
            axes[i].set_title(titles[i])
            
    # Hide empty subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")
        
    plt.tight_layout()
    plt.show()
