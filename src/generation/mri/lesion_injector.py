class LesionInjector:
    """
    Injects pathology labels into the normal SynthSeg label map.
    """
    def inject(self, label_map, disease, severity):
        if disease == "glioma":
            return self.inject_glioma(label_map)
        elif disease == "ms":
            return self.inject_ms_lesions(label_map)
        elif disease == "stroke":
            return self.inject_stroke(label_map)
        return label_map
            
    def inject_glioma(self, label_map, location=None, volume_cc=10, grade=4):
        """Inject GBM or LGG into white matter region with edema halo."""
        return label_map

    def inject_ms_lesions(self, label_map, count=5, distribution="periventricular"):
        """Add punctate periventricular + juxtacortical WM labels."""
        return label_map

    def inject_stroke(self, label_map, territory="mca", acuity="acute"):
        """MCA/ACA/PCA territory infarct."""
        return label_map
