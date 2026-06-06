# 🏥 Synthetic Medical Imaging Dataset Generator

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch 2.x](https://img.shields.io/badge/PyTorch-2.x-EE4C2C.svg)](https://pytorch.org/)
[![MONAI](https://img.shields.io/badge/MONAI-1.3+-00B5AD.svg)](https://monai.io/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-green.svg)](LICENSE)
[![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace_Spaces-yellow.svg)](#deployment)

> **Reference architecture:** [NVIDIA MAISI](https://developer.nvidia.com/maisi)
> **Hardware:** HP Omen · i5-13420H · NVIDIA RTX 4050 (6 GB VRAM)

A multi-modal synthetic medical imaging platform that generates realistic, physics-respecting,
and clinically-conditioned images across **7 imaging modalities**, **14 anatomy regions**, and
**55+ disease conditions**. Outputs are DICOM-compliant files with paired radiology reports,
disease heatmaps, segmentation masks, and structured JSON metadata.

---

## ✨ Key Features

- **7 Modalities:** X-ray, CT, MRI, Ultrasound, Mammography, Cardiac MRI, PET-CT
- **55+ Diseases:** From pneumonia to glioma to breast cancer — with radiologically accurate features
- **Physics-Correct Noise:** Rician (MRI), Poisson (CT), Rayleigh speckle (US), quantum+electronic (X-ray)
- **Rich Conditioning:** Disease ontology (SNOMED-CT), anatomy, severity, demographics, CT phase, scanner type
- **Automated QC:** nnU-Net anatomy validation + DenseNet-121 classifier confidence gating
- **DICOM Export:** Full clinical metadata, DICOM SR structured reports, synthetic watermarking
- **Paired Reports:** BioViL-T radiology text report generation
- **6 GB VRAM:** LoRA + FP16 + 8-bit optimizers + gradient checkpointing — runs on consumer GPUs

---

## 🏗️ Architecture

```
INPUT: modality + anatomy + disease + severity + [demographics]
    │
    ▼
[Layer 0]  Interface ─── CLI (typer) · REST API (FastAPI) · Demo (Gradio)
    │
[Layer 1]  Conditioning ─ Disease ontology · Anatomy · Severity · Demographics · Phase · Scanner
    │
[Layer 2]  Data ───────── 18 datasets · MONAI transforms · Modality-specific preprocessing
    │
[Layer 3]  Router ─────── Modality selector · Model registry · Config manager
    │
[Layer 4]  Generation ─── X-ray (LDM+ControlNet) · CT (VQVAE+2.5D LDM) · MRI (SynthSeg)
    │                      Ultrasound (speckle diffusion) · Mammography (view-conditioned)
    │                      Cardiac MRI (temporal cine) · Inpainting mode
    │
[Layer 4.5] Reports ───── BioViL-T report generation · DICOM SR
    │
[Layer 5]  QC ─────────── FID · SSIM · nnU-Net anatomy · DenseNet classifier · GradCAM heatmaps
    │
[Layer 6]  Post-process ─ Noise injection · Augmentation · DICOM generation
    │
[Layer 7]  Export ─────── DICOM/NIfTI/PNG/NRRD · Stratified splits · Auto-annotations
```

---

## 🚀 Quickstart

```bash
# Clone
git clone https://github.com/your-username/synthetic-med-imaging.git
cd synthetic-med-imaging

# Install
pip install -r requirements.txt

# Generate 50 chest X-rays with pneumonia
python generate.py --modality xray --anatomy chest \
  --disease pneumonia --severity moderate --count 50 \
  --format dicom --output ./dataset/

# Generate ultrasound of fatty liver
python generate.py --modality ultrasound --anatomy abdomen \
  --disease fatty_liver --probe curvilinear \
  --count 50 --format png --output ./dataset/

# Inpaint a nodule into an existing normal CT
python generate.py --mode inpaint \
  --base-image ./normal_ct.dcm \
  --mask ./roi_mask.nii.gz \
  --disease lung_nodule --severity moderate
```

---

## 📊 VRAM Budget

| Module | Operation | Peak VRAM |
|--------|-----------|-----------|
| X-ray LDM | LoRA training (512px, batch=4) | ~5.2 GB |
| CT VQVAE | Training (256px, batch=8) | ~3.2 GB |
| CT LDM | 2.5D training (latent, batch=4) | ~4.1 GB |
| Ultrasound | LoRA training (256px, batch=8) | ~3.5 GB |
| Mammography | LoRA training (512px, batch=4) | ~4.8 GB |
| nnU-Net QC | Inference only | ~2.0 GB |

All modules fit within **6 GB VRAM** using LoRA + FP16 + gradient checkpointing + 8-bit optimizer states.

---

## 📁 Project Structure

```
synthetic-med-imaging/
├── configs/           # YAML configs per modality + training
├── data/              # Datasets, splits, download scripts
├── src/
│   ├── interface/     # Layer 0: CLI, API, Gradio
│   ├── conditioning/  # Layer 1: Disease, anatomy, severity encoders
│   ├── data/          # Layer 2: Transforms, normalization
│   ├── routing/       # Layer 3: Model router, registry
│   ├── generation/    # Layer 4: X-ray, CT, MRI, US, Mammo, Cardiac, Inpaint
│   ├── reports/       # Layer 4.5: Report generation, DICOM SR
│   ├── quality/       # Layer 5: FID, nnU-Net, classifier QC
│   ├── postprocessing/# Layer 6: Noise, augmentation, DICOM gen
│   ├── export/        # Layer 7: Multi-format export
│   ├── privacy/       # Watermarking, DP, membership inference
│   └── utils/         # Logging, seeding, device management
├── training/          # Per-modality training scripts
├── notebooks/         # Jupyter exploration & demo notebooks
├── tests/             # Unit and integration tests
├── adapters/          # LoRA weights (gitignored)
└── outputs/           # Generated datasets (gitignored)
```

---

## 📜 License

Apache License 2.0 — see [LICENSE](LICENSE).

---

## 📖 References

- [NVIDIA MAISI](https://developer.nvidia.com/maisi) — Architectural reference
- [Stable Diffusion](https://arxiv.org/abs/2112.10752) — LDM backbone
- [SynthSeg](https://arxiv.org/abs/2107.09559) — MRI label synthesis
- [nnU-Net](https://www.nature.com/articles/s41592-020-01008-z) — Anatomy validation
- [MONAI](https://monai.io/) — Medical imaging framework
- [LoRA](https://arxiv.org/abs/2106.09685) — Parameter-efficient fine-tuning

---

*Project version: 2.0 · Hardware: HP Omen · RTX 4050 6GB*
