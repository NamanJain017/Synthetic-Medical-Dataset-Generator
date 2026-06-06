import os
import json

def format_bids_dataset(root_dir, dataset_name):
    """
    Organizes the generated files into the Brain Imaging Data Structure (BIDS) standard.
    """
    os.makedirs(root_dir, exist_ok=True)
    
    desc = {
        "Name": dataset_name,
        "BIDSVersion": "1.8.0",
        "DatasetType": "synthetic",
        "License": "CC-BY-4.0",
        "Authors": ["Synthetic Medical Dataset Generator"]
    }
    
    with open(os.path.join(root_dir, "dataset_description.json"), "w") as f:
        json.dump(desc, f, indent=4)
        
    print(f"BIDS dataset initialized at {root_dir}")
