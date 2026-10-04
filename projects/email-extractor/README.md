# Email Extractor

Finds email-like strings in clipboard text and replaces the clipboard contents with the matches, one per line.

## Run

Install `pyperclip`, then run:

```bash
python emailregx.py
```

The program reads and replaces clipboard contents. Its regular expression is a simple pattern, not a full email-address validator.