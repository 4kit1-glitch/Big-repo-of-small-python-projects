"""
    opening the top search results in my browser for a search made from my terminal 
    for now we do it with the https://pypi.org web page 
"""

import sys
import webbrowser
import bs4
import requests


BASE_URL = "https://pypi.org/search/?q="

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}


def get_search_html(query: str) -> str | None:
    try:
        response = requests.get(BASE_URL + query, timeout=10, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as err:
        print(f"failed to get response from {BASE_URL + query}: {err}")
        return None

def get_top_five_links(web_content: str) -> tuple:
    soup = bs4.BeautifulSoup(web_content, "html.parser")
    
    links = soup.select("a.package-snippet")[:5]

    links_str = [link.get("href") for link in links]

    return tuple(links_str)


        

def open_links(*links) -> None:
    for link in links:
        webbrowser.open_new_tab("https://pypi.org" + link)
        print(f"opened {link}")

def main():

    if len(sys.argv) < 2:
        print("no arg passed")
        sys.exit(0)

    query = "+".join(sys.argv[1:])

    print(f"Searching.....{query}")

    search_html = get_search_html(query)

    if search_html is None:
        print("error occured when searching")
        sys.exit(1)

    links = get_top_five_links(search_html)

    if not links:
        print("no links sent nothing to do ")
        sys.exit(0)

    open_links(*links)




if __name__ == "__main__":
    sys.exit(main())
