# System Architecture

The generator is built on an 8-Layer architecture inspired by NVIDIA MAISI.

1. **Layer 0 (Interface):** FastAPI, Gradio, CLI
2. **Layer 1 (Conditioning):** Disease Ontologies, Severity Encoders
3. **Layer 2 (Data Foundation):** Transforms, Normalization
4. **Layer 3 (Router):** Modality Routing, VRAM enforcement
5. **Layer 4 (Generation):** SD 2.1, MONAI VQVAE, SynthSeg
6. **Layer 4.5 (Reports):** BioViL-T text generation
7. **Layer 5 (Quality Control):** Pathology verification
8. **Layer 6/7/8 (Post-proc/Export/Privacy):** Artifact injection, DICOM writing, Watermarking
