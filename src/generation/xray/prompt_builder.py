def build_xray_prompt(anatomy, disease, severity, demographics=None):
    """
    Builds MIMIC-CXR style training prompt for X-ray generation.
    Format matches text-to-image conditioning expectations.
    """
    age_sex = ""
    if demographics:
        age_sex = f"{demographics.get('age', 'Unknown')}-year-old {demographics.get('sex', 'patient')}."
        
    return f"Chest radiograph, PA view. {age_sex} {disease}. Location: {anatomy}. Severity: {severity}."
