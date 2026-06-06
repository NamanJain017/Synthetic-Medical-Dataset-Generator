import numpy as np

def write_nifti(volume_tensor, output_path, affine=None):
    """
    Exports 3D volumes (CT, MRI) to NIfTI format for research tools
    like 3D Slicer or FSL.
    """
    try:
        import nibabel as nib
        if affine is None:
            affine = np.eye(4)
            
        if hasattr(volume_tensor, "numpy"):
            volume_tensor = volume_tensor.numpy()
            
        nii = nib.Nifti1Image(volume_tensor, affine)
        nib.save(nii, output_path)
        return True
    except ImportError:
        print("Warning: nibabel not installed. Skipping NIfTI write.")
        return False
