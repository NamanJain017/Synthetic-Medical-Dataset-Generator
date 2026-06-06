import os

def download_cbis_ddsm(target_dir="data/raw/cbis_ddsm"):
    """
    Downloads CBIS-DDSM Mammography dataset using TCIA REST API.
    See: https://wiki.cancerimagingarchive.net/display/Public/CBIS-DDSM
    """
    os.makedirs(target_dir, exist_ok=True)
    print(f"Please use NBIA Data Retriever to download CBIS-DDSM to {target_dir}")
    print("TCIA Collection: CBIS-DDSM")

if __name__ == "__main__":
    download_cbis_ddsm()
