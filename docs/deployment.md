# Deployment

## Local Deployment
Run the Gradio UI:
```bash
python src/interface/gradio_app.py
```

Run the API:
```bash
uvicorn src.interface.api:app --host 0.0.0.0 --port 8000
```

## Docker
(Coming Soon)
