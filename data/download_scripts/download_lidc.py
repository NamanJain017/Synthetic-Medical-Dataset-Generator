import os

def download_lidc_idri(target_dir="data/raw/lidc"):
    """
    Downloads LIDC-IDRI dataset using TCIA REST API or NBIA Data Retriever.
    See: https://wiki.cancerimagingarchive.net/display/Public/LIDC-IDRI
    """
    os.makedirs(target_dir, exist_ok=True)
    print(f"Please use NBIA Data Retriever to download LIDC-IDRI to {target_dir}")
    print("TCIA Collection: LIDC-IDRI")

if __name__ == "__main__":
    download_lidc_idri()
