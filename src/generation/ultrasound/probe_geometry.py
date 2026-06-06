PROBE_TOKENS = {
    "linear":       0,  # Vascular, MSK, breast, thyroid  → rectangular FOV
    "curvilinear":  1,  # Abdomen, pelvis, OB/GYN         → fan-shaped FOV
    "phased_array": 2,  # Cardiac, transcranial           → sector FOV
    "endocavitary": 3,  # Transvaginal, transrectal       → wide-angle sector
    "linear_hockey":4,  # High-frequency vascular         → small footprint
}

def apply_probe_mask(image, probe_type):
    """
    Applies the appropriate geometric mask to simulate the probe's field of view.
    """
    return image
