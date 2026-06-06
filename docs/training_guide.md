# Training Guide

This project uses Parameter-Efficient Fine-Tuning (PEFT) with LoRA to stay within a strict 6GB VRAM budget.

## Setup
1. Ensure your dataset is downloaded and structured via BIDS.
2. Adjust `configs/training/*.yaml` for your modality.

## Running Training
Run the specific script for your target modality:
```bash
python training/train_xray_lora.py
```

## VRAM Monitoring
The scripts will automatically enforce gradient checkpointing, 8-bit optimizers (bitsandbytes), and batch size accumulation.
