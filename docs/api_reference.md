# API Reference

The Synthetic Medical Dataset Generator exposes a REST API via FastAPI.

## Endpoints

### `POST /generate`
Queues a generation job.
**Body:** `GenerationRequest`
**Returns:** `JobStatus` (includes `job_id`)

### `GET /status/{job_id}`
Poll this endpoint to track generation progress.
**Returns:** `JobStatus`

### `GET /download/{job_id}`
Download the generated dataset as a zip file once completed.

### `GET /health`
Returns system status, GPU availability, and free VRAM.
