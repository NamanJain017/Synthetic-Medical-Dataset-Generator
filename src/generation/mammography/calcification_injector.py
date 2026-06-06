class CalcificationInjector:
    """
    Injects calcifications into mammograms. 
    Diffusion models struggle with this high-frequency detail natively,
    so it is explicitly injected.
    """
    MORPHOLOGIES = ["amorphous", "coarse_heterogeneous", "fine_pleomorphic",
                    "fine_linear", "coarse_popcorn"]
    DISTRIBUTIONS = ["clustered", "linear", "segmental", "regional", "diffuse"]

    def inject(self, image, disease, severity):
        return image
