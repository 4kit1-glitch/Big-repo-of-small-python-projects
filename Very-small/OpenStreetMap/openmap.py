"""
program automatically opens a street address in open steet map.org 

"""

import sys
import webbrowser
from urllib.parse import urlparse, quote_plus


file_path = sys.argv[0]
BASE_URL = "https://www.openstreetmap.org"


def is_valid_web(page) -> bool:
    # i dont really need this adding the url checker was just for learning processes
    result = urlparse(page)
    # all web pages need a scheme that is https/http and a netloc, thats the rest of the url
    return all((result.scheme, result.netloc))

def open_web(page):
    if is_valid_web(page):
        print(f"opening page: {page}")
        webbrowser.open(page)
    else:
        print(f"Invalid page: {page}", sys.stderr)
        return False

    return True
    
def main() -> int:    
    if len(sys.argv) == 1:
        print("Must a street address", file=sys.stderr)
        sys.exit(1)

    raw_addr = " ".join(sys.argv[1:])
    encoded_addr = quote_plus(raw_addr)

    full_addr = f"{BASE_URL}/search?query={encoded_addr}"

    if not open_web(full_addr):
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
