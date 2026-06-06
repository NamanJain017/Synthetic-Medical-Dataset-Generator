from monai.networks.nets import AutoencoderKL

def get_vqvae():
    """
    Returns the VQVAE for compressing 256x256 CT slices -> 32x32 latents.
    This enables 8x spatial compression for the 2.5D LDM.
    """
    return AutoencoderKL(
        spatial_dims=2, 
        in_channels=1, 
        out_channels=1,
        num_channels=(128, 256, 512), 
        latent_channels=4,
        num_res_blocks=2, 
        norm_num_groups=32,
        attention_levels=(False, False, True),
    )
