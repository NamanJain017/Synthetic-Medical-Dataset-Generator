import os

def download_echonet_dynamic(target_dir="data/raw/echonet"):
    """
    Downloads EchoNet-Dynamic Dataset.
    Requires Stanford ML Group registration.
    """
    os.makedirs(target_dir, exist_ok=True)
    print(f"Register at https://echonet.github.io/dynamic/ to receive download link.")
    print(f"Extract EchoNet-Dynamic zip into {target_dir}")

if __name__ == "__main__":
    download_echonet_dynamic()
