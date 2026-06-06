import uuid
from typing import Optional, Dict
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from .schemas import GenerationRequest, InpaintRequest, JobStatus
import os

app = FastAPI(
    title="Synthetic Medical Imaging API",
    description="Generate conditioned synthetic medical images across 7 modalities",
    version="2.0.0"
)

jobs: Dict[str, dict] = {}

def export_results(images, output_dir, fmt, metadata):
    os.makedirs(output_dir, exist_ok=True)
    paths = []
    # Dummy integration with our export module
    from src.export.png_writer import write_png
    for i, img in enumerate(images):
        path = os.path.join(output_dir, f"img_{i}.png") # simplifying to PNG for scaffolding
        write_png(img, path)
        paths.append(path)
    return paths

async def run_generation(job_id: str, request: GenerationRequest):
    jobs[job_id]["status"] = "running"
    jobs[job_id]["progress"] = 0

    try:
        from src.routing.modality_router import ModalityRouter
        from src.quality.qc_pipeline import QualityControlPipeline

        router = ModalityRouter()
        pipeline = router.get_pipeline(request.modality)

        outputs = []
        for i in range(request.count):
            # Call generation engine
            image = pipeline.generate(
                anatomy=request.anatomy,
                disease=request.disease,
                severity=request.severity,
                # additional args omitted for brevity
            )
            outputs.append(image)
            jobs[job_id]["progress"] = int((i + 1) / request.count * 80)

        # QC pass
        qc = QualityControlPipeline()
        validated = []
        for img in outputs:
            res = qc.run_qc(img, None, request.anatomy, request.disease, request.severity)
            if res["status"] == "PASSED":
                validated.append(img)
                
        jobs[job_id]["progress"] = 90

        # Export
        output_dir = f"./outputs/{job_id}"
        paths = export_results(
            validated, 
            output_dir, 
            request.format,
            {"modality": request.modality, "disease": request.disease}
        )

        jobs[job_id].update({
            "status": "done",
            "progress": 100,
            "count": len(paths),
            "download_url": f"/download/{job_id}",
            "output_dir": output_dir,
        })

    except Exception as e:
        jobs[job_id].update({"status": "failed", "error": str(e)})


@app.post("/generate", response_model=JobStatus)
async def generate(request: GenerationRequest, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    jobs[job_id] = {"status": "queued", "progress": 0}
    background_tasks.add_task(run_generation, job_id, request)
    return JobStatus(job_id=job_id, status="queued", progress=0)


@app.get("/status/{job_id}", response_model=JobStatus)
async def get_status(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    j = jobs[job_id]
    return JobStatus(
        job_id=job_id,
        status=j["status"],
        progress=j.get("progress", 0),
        count=j.get("count"),
        download_url=j.get("download_url"),
        error=j.get("error"),
    )

@app.get("/download/{job_id}")
async def download(job_id: str):
    import shutil
    if job_id not in jobs or jobs[job_id]["status"] != "done":
        raise HTTPException(status_code=404, detail="Job not ready")
    output_dir = jobs[job_id]["output_dir"]
    zip_path = shutil.make_archive(f"outputs/{job_id}", "zip", output_dir)
    return FileResponse(zip_path, media_type="application/zip", filename=f"synthetic_{job_id[:8]}.zip")
