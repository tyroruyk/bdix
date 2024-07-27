import requests
from tqdm import tqdm


def accessibility(url):
    try:
        # simulate a long-running operation with tqdm
        for _ in tqdm(range(1), desc="Pinging {0}".format(url)):
            response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except Exception:
        return False
