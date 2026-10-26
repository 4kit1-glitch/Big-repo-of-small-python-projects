# a simple commic downloader for the https://xkcd​.com website


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
    
    

def url_to_filename():
    

def download_image(url: str) -> Path:
    try:
        response = requests.get(url, timeout=10, headers=HEADERS)

        STORE_PATH.mkdir(parents=True, exist_ok=True)

        Path.touch(url.strip(""))
    pass

def main():
    prev_link = ""
    num = 0

    print("Starting...")
    while True:
        if prev_link == "#":
            break

        web_str = get_html(BASE_URL + prev_link)
        prev_link = get_prev_link(web_str)
        download_image(get_img_link(web_str))

        num += 1
    

    print(f"download complete {num} commics downloaded to {STORE_PATH}")



if __name__ == "__main__":
    main()
    
