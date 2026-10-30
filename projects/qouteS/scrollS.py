import bs4, requests
from pathlib import Path
from json import load

BASE_URL = "https://quotes.toscrape.com/scroll"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.8",
    "Referer": "https://quotes.toscrape.com/scroll",
    "X-Requested-With": "XMLHttpRequest",
}

def get_page_url() -> str:
    pass

def get_page_data(url) -> dict:
    pass

def get_qoute() -> str:
    pass

def get_author() -> str:
    pass

def perform_save() -> None:
    pass

def main():
    pass

if __name__ == "__main__":
    main()
