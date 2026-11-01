import requests
import bs4
import json


BASE_URL = "https://quotes.toscrape.com/js"


def get_html(url: str) -> str | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as err:
        print(f"Failed to get page html {err}")
        return None

def get_data(web_content: str) -> None | list:
    try:
        soup = bs4.BeautifulSoup(web_content, "html.parser")

        script_content = soup.find("script")

        data_script = script_content.find_next_sibling() if script_content else None

        data_text = data_script.text.strip() if data_script else None

        if data_text is None:
            return None
        
        data_list = data_text.split("var data =", maxsplit=1)[1].strip()



        decoder = json.JSONDecoder()

        obj, _dummy = decoder.raw_decode(data_list)


        if not isinstance(obj, list):
            print(f"Expected list got {type(obj).__name__}")
            raise TypeError

        return obj
            
    except (TypeError, IndexError):
        print(f"Failed top extract page data: {err}")

def save_quotes():
    pass

def get_next_url():
    pass