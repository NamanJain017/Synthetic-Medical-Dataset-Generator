def build_mammography_prompt(disease, view, birads):
    """
    Builds conditioning text for mammography.
    """
    return f"Mammogram, {view.upper()} view. Disease: {disease}. ACR BIRADS score: {birads}."
