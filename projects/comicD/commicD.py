# a simple commic downloader for the https://xkcd​.com website


import re
import random
import requests
import bs4

from pathlib import Path
from time import sleep
from urllib.parse import urlparse


BASE_URL = "https://xkcd.com"

STORE_PATH = Path.cwd() / "downloaded_comics"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}


def get_html(url: str) -> str | None:
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None

def get_img_link(html_content: str) -> str | None:
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    try:
        link = str(soup.select("br a")[1].get("href"))
        return link
    except IndexError:
        return
    
def get_prev_link(html_content: str) -> str | None:
    soup = bs4.BeautifulSoup(html_content, "html.parser")

    link_tag = soup.select_one("a[rel='prev']")

    if link_tag:
        link = link_tag.get("href")
        link = BASE_URL + str(link) if link else None

        return link
    
    

def url_to_filename(url: str) -> str:
    parsed_url = urlparse(url)

    raw_name = parsed_url.netloc if parsed_url.netloc else parsed_url.path

    raw_name.rstrip("/")

    safe_name = re.sub(r'[^a-zA-Z0-9\.\-]', '_', raw_name)

    return safe_name if safe_name else "unamed"


def download_image(url: str) -> None:
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)
        response.raise_for_status()

        STORE_PATH.mkdir(parents=True, exist_ok=True)

        filepath = STORE_PATH / f"{url_to_filename(url)}.png"

        Path.touch(filepath, exist_ok=True)

        with filepath.open("w+b") as file:
            file.write(response.content)
    except requests.RequestException:
        pass
    except OSError:
        pass

    

def main():
    prev_link = ""
    num = 0

    print("Starting...")
    while True:
        if prev_link == "#" or prev_link is None:
            break

        web_str = get_html(BASE_URL + prev_link)

        if web_str is None:
            break

        prev_link = get_prev_link(web_str)
        img_lnk = get_img_link(web_str)

        if not img_lnk:
            break

        download_image(img_lnk)

        num += 1
    

    print(f"download complete {num} commics downloaded to {STORE_PATH}")



if __name__ == "__main__":
    main()
    
