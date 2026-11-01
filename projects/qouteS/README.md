# Quotes Project

A small Python project for collecting quotes from Quotes to Scrape and presenting a local quote collection as a terminal slideshow. It includes a working paginated scraper, an in-progress parser for the JavaScript-rendered page, and a terminal-based slideshow.

## Requirements

- Python 3.10 or later
- `requests` for the paginated scraper and the JavaScript-page helper
- `beautifulsoup4` for the JavaScript-page helper
- `pygame` is optional and enables the slideshow's background audio integration

Install the required packages from the project directory:

```bash
python -m pip install requests beautifulsoup4
```

To enable audio in the slideshow, install `pygame` as well:

```bash
python -m pip install pygame
```

Alternatively, activate the project's virtual environment before installing or running the scripts:

```bash
source .venv/bin/activate
```

## Scripts

### `scrollS.py`

Downloads quotes from the Quotes to Scrape API one page at a time. Each quote is saved on its own line. When all pages have been retrieved, the script writes the clean collection to `quotes/quotes.complete.txt`.

```bash
python scrollS.py
```

The scraper records its most recently completed page in `quotes/quotes.partial.txt`. If interrupted, run it again to continue from the next page. After a successful download, it removes the progress file. Network or extraction errors stop the current run while retaining progress for a later retry.

### `jsS.py`

The HTTP request helper, `get_html()`, is implemented and retrieves the JavaScript-rendered quotes page using `requests`. The `get_data()` function uses Beautiful Soup to find the embedded `var data =` script content, decode its JSON value, and return it as a list. This retrieves the page's quote data, but the list is not yet processed into individual quote records for use or saving. Completing that quote handling, along with saving and pagination, remains future work.

This script is **not yet a complete scraper**: it has no command-line entry point, and the saving and next-page functions are unfinished. Running `python jsS.py` by itself does not fetch or save quotes. The current parsing error handler also needs correction before it can reliably report malformed page data.

### `slide_show.py`

Reads `quotes/quotes.complete.txt` and displays each nonblank line in the terminal with a fade-in/fade-out effect. The slideshow pauses between quotes and handles Ctrl+C by restoring the terminal cursor before exiting. It can also use optional background audio when `pygame` and the configured audio resource are available; without `pygame`, the quotes still display.

```bash
python slide_show.py
```

The slideshow expects the complete quote collection to exist before it starts. Press Ctrl+C to stop it early.

## Running the Project

Run commands from the project root so the scripts resolve their data paths correctly:

```bash
python scrollS.py
python slide_show.py
```

The scraper creates the `quotes` directory as needed. The slideshow reads the completed collection from that directory and reports an error if it is missing or empty.

## Data and Path Behavior

The scraper and slideshow build their file paths from the current working directory. Running them from another directory may cause them to look for or create quote data in the wrong location. Start them from the project root.

The complete quote file is plain text, with one quote per line. The partial file is an internal resume file and includes page markers between downloaded batches; the scraper removes these markers when it creates the completed collection.