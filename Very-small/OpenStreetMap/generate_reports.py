import webbrowser
from pathlib import Path

log_path = Path.cwd() / "test.log"

with log_path.open("w") as file:
    file.write("<h1>HELLO WORLD</h1>")

webbrowser.open(str(log_path))