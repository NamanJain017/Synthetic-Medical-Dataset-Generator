# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] — 2025-06-15

### Added
- **Ultrasound module** with Rayleigh speckle model and probe conditioning
- **Mammography module** with CC/MLO view conditioning and BIRADS scoring
- **Cardiac MRI module** with temporal cine diffusion
- **PET-CT module** with SUV conditioning
- **Inpainting mode** for pathology injection into existing scans
- **Image-to-image mode** for disease augmentation
- **Radiology report generation** via BioViL-T
- **DICOM Structured Reports** (DICOM SR)
- **Tree-Ring watermarking** for synthetic image provenance
- **Differential privacy** support via Opacus
- **Membership inference testing** for privacy verification
- **Demographics conditioning** (age, sex)
- **Multi-phase CT conditioning** (arterial, venous, delayed, etc.)
- **Scanner harmonization** tokens (GE, Siemens, Philips)
- **Comorbidity conditioning** for multi-disease generation
- **GradCAM disease heatmaps**
- **Radiomics feature extraction** via pyradiomics
- **Docker containerization** with GPU support
- **HuggingFace Spaces** deployment config
- 11 new datasets added to the registry (18 total)
- 27 new diseases added (55+ total)
- 8 new anatomy regions (14 total)

## [1.0.0] — 2025-05-01

### Added
- Initial 8-layer architecture
- X-ray generation (SD 2.1 + ControlNet + LoRA)
- CT generation (2.5D VQVAE + LDM)
- MRI generation (SynthSeg + contrast synthesis)
- Disease ontology conditioning (SNOMED-CT)
- Anatomy encoder and severity CFG
- FID, SSIM quality metrics
- nnU-Net anatomy validation
- DenseNet-121 pathology verification
- DICOM export with full metadata
- NIfTI, PNG, NRRD export
- Stratified dataset splitting
- CLI (typer) and REST API (FastAPI)
