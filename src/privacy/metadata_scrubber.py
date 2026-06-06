def scrub_metadata(metadata_dict):
    """
    Ensures that no real patient PHI accidentally leaks into the 
    synthetic dataset's metadata. 
    Overrides PatientName, PatientID, DOB, etc., with synthetic placeholders.
    """
    safe_dict = metadata_dict.copy()
    safe_dict["PatientName"] = "SYNTHETIC^PATIENT"
    safe_dict["PatientID"] = "SYNTH_000000"
    safe_dict["PatientBirthDate"] = "19000101"
    return safe_dict
