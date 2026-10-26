# PyPI Search Opener

A small command-line tool that searches [PyPI](https://pypi.org/) and opens the first five matching package pages in your default browser.

## Requirements

- Python 3.10 or newer
- `requests`
- `beautifulsoup4`

Install the dependencies with:

```bash
python3 -m pip install requests beautifulsoup4
```

## Usage

Pass the package search terms as command-line arguments:

```bash
python3 OAS.py selenium
```

For multiple words, quote the phrase or pass the words separately. Both forms are joined into a PyPI search query:

```bash
python3 OAS.py "web testing"
python3 OAS.py web testing
```

The script prints the search query and opens up to five results in new browser tabs. If no search terms are provided, it prints a message and exits.

## Files

- `OAS.py` - PyPI search and browser-opening CLI.
- `test.py` - Small standalone list-slicing example; it is not currently a test suite for `OAS.py`.