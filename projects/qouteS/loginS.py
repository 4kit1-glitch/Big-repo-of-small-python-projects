# this is practices scraping through a login and credentials page

import requests
import bs4

BASE_URL = "https://quotes.toscrape.com/login"


def get_csrf_tocken(my_session: requests.Session) -> None | str:
    # start a session use a with open statement to keep it in check
    
        # get the login page and get csrf_tocken
    try:
        response = my_session.get(BASE_URL, timeout=10)
        response.raise_for_status()

        soup = bs4.BeautifulSoup(response.text, "html.parser")

        tocken_tag = soup.find("input",attrs={"name": "csrf_token"})
        
        if not tocken_tag :
            raise KeyError

        tocken = str(tocken_tag["value"])
            
        return tocken
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Failed to get csrf_tocken: {e}")
        return None


def build_payload(session: requests.Session, username: str, password: str) -> dict | None:
    token = get_csrf_tocken(session)

    if token is None:
        return None

    return {"username": username, "password": password, "csrf_token": token}


def login_and_scrape(username: str, passwd: str) -> bool:
    with requests.session() as my_session:
        payload = build_payload(my_session, username, passwd)
        if payload is None:
            return False

        try:
            response = my_session.post(BASE_URL, data=payload, timeout=10)
            response.raise_for_status()

            if "logout" in response.text:
                print("logged in successfully")
                return True

            else: 
                print("login failed")

            return False
        except requests.RequestException as err:
            print(f"Login failed: {err}")
            return False

login_and_scrape(username="admin", passwd="password123")