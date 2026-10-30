import bs4, requests
from pathlib import Path


BASE_URL = "https://quotes.toscrape.com/api/quotes"

PARTIAL_PATH = Path.cwd() / "qoutes" /"qoutes.partial.txt"
FULL_PATH = Path.cwd() / "quotes" / "qoutes.complete.txt"

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


def get_current_page_num(data: dict) -> int | None:
    return data.get("page")
    


def get_qoutes(data: dict) -> list | None:
    try:
        quotes_data = data["quotes"]
        quotes = [ quote.get("text", "").strip("“”") for quote in quotes_data ]
        return quotes
    except KeyError:
        print("Text key not found")
        return None
    except TypeError:
        print("Text type not a string")
        return None


def is_next_present(data: dict) -> bool:
    return bool(data.get("has_next"))

def perform_save(quotes: list, path: Path) -> None:
    for quote in quotes:
        with path.open("a") as file:
            file.write(quote)

            


def main():
    current_page_num = 1

    print("starting")

    while True:

        print(f"page {current_page_num}")
        pg_data = get_page_data(url=BASE_URL, page_num=current_page_num)    # page data

        if not pg_data:
            print(f"Server error: \t Failed to fetch data from page: {current_page_num}")
            break

        current_page_num = get_current_page_num(pg_data)

        if not current_page_num:
            print("could not auto get next page number from data")
            break

        qoutes = get_qoutes(data=pg_data)

        if not qoutes:
            print("could not auto get next page number from data")
            break

        perform_save(qoutes, path=PARTIAL_PATH)

        if not is_next_present(pg_data):
            print("No page left")
            PARTIAL_PATH.rename(FULL_PATH)
        
    

    





if __name__ == "__main__":
    main()
