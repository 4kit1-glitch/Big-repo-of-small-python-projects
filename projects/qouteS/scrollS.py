import bs4, requests
from pathlib import Path
BASE_URL = "https://quotes.toscrape.com/scroll"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.8",
    "Referer": "https://quotes.toscrape.com/scroll",
    "X-Requested-With": "XMLHttpRequest",
}

def get_page_data(url: str, page_num: int) -> dict | None:
    try:
        response = requests.get(url, headers=HEADERS, params={"page": page_num}, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            print(f" Expected dict, got {type(data.__name__)}")
            return None

        return data
    except requests.RequestException as err:
        print(f"failed to get page {page_num} data: {err}")
        return None



def get_qoutes(data: dict, page_num: int) -> list | None:
    try:
        return data["quotes"]
    except KeyError:
        return None


def is_next_present(data: dict) -> bool:
    pass

def perform_save(qoute: str) -> None:
    pass

def main():
    pass

if __name__ == "__main__":
    main()
