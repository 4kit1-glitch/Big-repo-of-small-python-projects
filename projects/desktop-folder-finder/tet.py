
from pathlib import Path
import os


direct = Path("Desktop")
home = Path.home()

for current_root, dirs, files in os.walk(home / "Desktop", topdown=True):
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    for d in dirs:
        if "desktop" in d.lower():
            print(Path(d))
        

