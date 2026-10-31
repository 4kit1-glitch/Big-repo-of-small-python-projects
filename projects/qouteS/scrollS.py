import sys
import requests
from pathlib import Path
from collections import deque


BASE_URL = "https://quotes.toscrape.com/api/quotes"

PARTIAL_PATH = Path.cwd() / "quotes" /"quotes.partial.txt"
FULL_PATH = Path.cwd() / "quotes" / "quotes.complete.txt"

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

def perform_save(quotes: list, path: Path, page_num: int) -> None:
    path.parent.mkdir(exist_ok=True, parents=True)
    with path.open("a", encoding="utf-8") as file:
        for quote in quotes:
            file.write(f"{quote}page{page_num}\n")





def get_last_page_num(filename: Path) -> int:
    with filename.open("r", encoding="utf-8") as file:
        last_line = deque(file, maxlen=1)[0]


    return int(last_line.strip().split("page")[1])


    

    

def is_partial_exist():
    return PARTIAL_PATH.exists()



def main(start_page_num: int = 1):
    current_page_num = start_page_num

    print("starting...")

    while True:

        print(f"page {current_page_num}")
        pg_data = get_page_data(url=BASE_URL, page_num=current_page_num)    # page data

        if not pg_data:
            print(f"Server error: \t Failed to fetch data from page: {current_page_num}")
            break


        qoutes = get_qoutes(data=pg_data)

        if not qoutes:
            print("could not auto get next page number from data")
            break

        perform_save(qoutes, path=PARTIAL_PATH, page_num=current_page_num)

        if not is_next_present(pg_data):
            print("No pages left. Finalizing file...")

            # Handle the rename safely
            if FULL_PATH.exists():
                FULL_PATH.unlink()

            PARTIAL_PATH.rename(FULL_PATH)

            print("Download complete!")
            break

        current_page_num += 1

def resume_partial() -> None:
    last_page = get_last_page_num(PARTIAL_PATH)

    print(f"resuming from page {last_page}")
    main(last_page + 1)



if __name__ == "__main__":
    if is_partial_exist():
        sys.exit(resume_partial())
    sys.exit(main())