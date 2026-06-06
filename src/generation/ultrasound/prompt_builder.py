def build_ultrasound_prompt(anatomy, disease, severity, probe):
    """
    Builds the conditioning text prompt for Ultrasound generation.
    """
    return f"Ultrasound, {probe} probe. Anatomy: {anatomy}. Disease: {disease}. Severity: {severity}."
