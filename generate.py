#!/usr/bin/env python3
"""
Synthetic Medical Imaging Dataset Generator — CLI Entry Point.

Top-level script that wraps the typer CLI application defined in src.interface.cli.
This is the primary user-facing entry point for the project.

Usage:
    python generate.py --modality xray --anatomy chest --disease pneumonia \
        --severity moderate --count 50 --format dicom --output ./dataset/

    python generate.py --modality ultrasound --anatomy abdomen \
        --disease fatty_liver --probe curvilinear --count 50 --format png

    python generate.py --mode inpaint --base-image ./normal_ct.dcm \
        --mask ./roi_mask.nii.gz --disease lung_nodule --severity moderate
"""

import sys
from pathlib import Path

# Ensure the project root is on the Python path
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.interface.cli import app

if __name__ == "__main__":
    app()
