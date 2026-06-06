from pydantic import BaseModel, Field
from typing import Literal, Optional

class GenerationRequest(BaseModel):
    modality: Literal["xray","ct","mri","ultrasound","mammography","cardiac_mri","pet_ct"]
    anatomy:  str = Field(..., example="chest")
    disease:  str = Field(..., example="pneumonia")
    severity: Literal["mild","moderate","severe","all"] = "moderate"
    count:    int  = Field(default=10, ge=1, le=500)
    format:   Literal["dicom","nifti","png","nrrd"] = "dicom"

    # Optional conditioning signals
    age:      Optional[int]   = Field(default=None, ge=0, le=120)
    sex:      Optional[Literal["male","female"]] = None
    contrast: Optional[Literal["t1","t2","flair","dwi","swi"]] = None
    phase:    Optional[Literal["non_contrast","arterial","portal_venous","delayed"]] = None
    probe:    Optional[Literal["linear","curvilinear","phased_array"]] = None
    birads:   Optional[int]  = Field(default=None, ge=1, le=6)
    with_report: bool = False
    seed:     Optional[int]  = None

class InpaintRequest(BaseModel):
    base_image_path: str
    mask_path:       str
    disease:  str
    severity: Literal["mild","moderate","severe"] = "moderate"
    seed:     Optional[int] = None

class JobStatus(BaseModel):
    job_id:       str
    status:       Literal["queued","running","done","failed"]
    progress:     int = 0          # 0–100
    count:        Optional[int] = None
    download_url: Optional[str] = None
    error:        Optional[str] = None
