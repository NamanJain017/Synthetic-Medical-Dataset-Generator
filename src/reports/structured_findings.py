def generate_structured_findings(disease, severity, anatomy, modality):
    """
    Translates ontology data into structured JSON findings suitable 
    for serialization into a DICOM SR (Structured Report).
    """
    return {
        "Diagnosis": disease,
        "Severity": severity,
        "Anatomy": anatomy,
        "Modality": modality,
        "Confidence": "1.0 (Synthetic Ground Truth)",
        "IsSynthetic": True
    }
