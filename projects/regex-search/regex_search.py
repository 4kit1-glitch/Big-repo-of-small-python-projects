# program opens all files in the text files in a folder
# it gets a line from the user 
# then searches each file for
# that line and prints the files names with that line

import sys
import os
from pathlib import Path
import re

def is_pattern_in_file(pattern: str, file_path: Path) -> bool:
    pat = re.compile(rf'{pattern}', re.IGNORECASE)
    with file_path.open("r", encoding="utf-8") as file:
        all_lines = file.readlines()

    if not all_lines:
        return False
    for line in all_lines:
        if pat.findall(line):
            return True
    return False


def get_directory(dir_name: str) -> Path:
    dir_path = Path(dir_name)
    root = Path.home()

    if dir_path.is_absolute():
        if dir_path.is_dir():
                return dir_path
        print(f"Folder: {dir_path} not found")
        sys.exit(2)

    for current_root, dirs, files in os.walk(root , topdown=True):
        print(len(dirs))

        


get_directory("desktop")


def main():
    directory = input("Enter the dir to search in: ")
    directory = get_directory(directory)
    pattern = input("Enter word to match or pattern: ")