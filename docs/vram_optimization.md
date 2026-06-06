# VRAM Optimization

This architecture is explicitly designed for consumer GPUs (e.g., RTX 4050 6GB).

## Techniques Used
1. **LoRA (Low-Rank Adaptation):** Only a tiny fraction of parameters are trained.
2. **2.5D Auto-Regressive Generation:** Full 3D generation takes 40GB+ VRAM. We compress spatial dimensions using VQVAE (8x) and generate slice-by-slice.
3. **8-bit Optimizers:** Reduces Adam state memory.
4. **Gradient Checkpointing:** Trades compute time for memory savings.
