import torch
import numpy as np
import random
import os

def set_seed(seed: int = 42):
    """
    Sets global deterministic seed for reproducibility across 
    PyTorch, NumPy, and Python's random module.
    """
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        
        # Optimize for reproducibility
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
