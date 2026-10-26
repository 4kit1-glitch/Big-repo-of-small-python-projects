# a simple commic downloader for the https://xkcd​.com website

import requests
import bs4

from pathlib import Path


BASE_URL = "https://xkcd.com"

STORE_PATH = Path.cwd() / "downloaded_comics"


def get_html(url: str) -> str:
    pass

def get_img_link(html_content: str) -> str:
    pass

def get_prev_link(html_content: str) -> str:
    pass

def download_image(url: str) -> Path:
    pass

def main():
    prev_link = ""
    while True:
        web_str = get_html(BASE_URL + prev_link)
        prev_link = get_prev_link(web_str)



        print("Starting download")
    
