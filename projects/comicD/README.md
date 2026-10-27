# comicD

A lightweight Python utility for downloading comics from XKCD and saving them locally on your machine.

## Overview

`comicD` is a simple script that crawls the XKCD archive, follows each comic's previous-link chain, and downloads the associated image files. It is designed to be easy to run, easy to customize, and useful as a starting point for learning web scraping, HTTP requests, and local file downloads in Python.

## Features

- Downloads XKCD comic images automatically
- Traverses the archive by following each comic's previous page link
- Uses a browser-like user agent to reduce request issues
- Saves images to a local output directory on disk
- Includes graceful handling for network and file errors
- Keeps the implementation intentionally simple and readable

## Requirements

- Python 3.9+
- `requests`
- `beautifulsoup4`

## Installation

1. Clone or download this project to your local machine.
2. Open a terminal in the project directory.
3. Install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the project root:

```bash
python commicD.py
```

The script will begin downloading comics from the XKCD site and save them into a local folder created during execution.

## Behavior

The program:

1. Requests the XKCD homepage.
2. Extracts the comic image URL from the page.
3. Follows the "previous" comic link.
4. Repeats until there are no more previous comics.
5. Saves each downloaded image to disk.

This makes it a straightforward example of a small, archive-based downloader.

## Project Structure

```text
comicD/
├── README.md
├── commicD.py
└── downloaded_comics/   # created at runtime by the script
```

> The `downloaded_comics` directory is generated during execution and is not part of the source documentation.

## Notes

- The script uses a randomized delay between requests to avoid hammering the site.
- Network failures or invalid pages are handled with messages instead of crashing the program.
- This project is intentionally minimal and can serve as a foundation for more advanced download tools, scheduling, or batch processing.

## License

This project is provided for educational and personal use. Please respect the terms and usage policies of the source website.
