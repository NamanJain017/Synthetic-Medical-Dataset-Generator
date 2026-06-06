import torch
import gc

def get_device():
    """
    Auto-detects the optimal device (CUDA, MPS, or CPU).
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        return torch.device("cpu")

def clear_vram():
    """
    Clears PyTorch CUDA cache and runs garbage collection.
    Useful for staying within the 6GB VRAM limit.
    """
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

def get_vram_usage():
    """
    Returns current VRAM usage in MB (allocated, reserved).
    """
    if not torch.cuda.is_available():
        return 0, 0
    
    allocated = torch.cuda.memory_allocated() / (1024 ** 2)
    reserved = torch.cuda.memory_reserved() / (1024 ** 2)
    return allocated, reserved

def check_vram_requirements(required_gb: float) -> bool:
    """
    Checks if the system has enough VRAM available.
    Specifically targetting the 6GB RTX 4050 constraint.
    """
    if not torch.cuda.is_available():
        print("Warning: CUDA not available. Running on CPU may be extremely slow.")
        return True

    # Total device memory in GB
    total_mem_gb = torch.cuda.get_device_properties(0).total_memory / (1024 ** 3)
    
    # Check if the requested amount exceeds total physical VRAM
    if required_gb > total_mem_gb:
         raise RuntimeError(
             f"Insufficient VRAM: Module requires {required_gb}GB, "
             f"but device only has {total_mem_gb:.1f}GB available."
         )
    
    return True
