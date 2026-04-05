import requests
import os

def download_image(url, save_path):

    if not isinstance(url, str) or not url.startswith("http"):
        print(f"[SKIP IMAGE] Invalid URL: {url}")
        return None

    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(save_path, "wb") as f:
            f.write(response.content)

        return save_path

    except Exception as e:
        print(f"[IMAGE DOWNLOAD FAILED] {e}")
        return None