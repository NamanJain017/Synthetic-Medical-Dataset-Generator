# Quality Control (QC) Pipeline

Every generated image must pass through `src/quality/qc_pipeline.py`.

## Validation Steps
1. **Anatomy Validation:** nnU-Net ensures the gross anatomical structure (e.g., lungs, heart) is clinically plausible.
2. **Pathology Verification:** A downstream DenseNet classifier verifies that the requested disease is actually present.
3. **Radiomics:** Feature extraction confirms statistical similarity to real tumors.
4. **Heatmaps:** GradCAM ensures the classifier triggers on the correct anatomical region.
