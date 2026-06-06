FROM pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application code
COPY src/ ./src/
COPY configs/ ./configs/
COPY generate.py .

# LoRA adapters must be mounted or copied separately (large files)
# COPY adapters/ ./adapters/

# Output directory
RUN mkdir -p /app/outputs

EXPOSE 8000 7860

# Default: run FastAPI server
CMD ["uvicorn", "src.interface.api:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
