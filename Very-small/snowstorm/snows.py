#!/usr/bin/python3

import os
import random 
import subprocess
import sys
import time


TOP = chr(9600)
BOTTOM = chr(9604)
FULL = chr(9608)


def set_desity() -> int:
    try:
        density = int(input("enter density(0-99): "))
    except ValueError:
        print("invalid input..")
        sys.exit(1)
    return density

def set_density2() -> int:
    if len(sys.argv) > 1:
        try:
            density = int(sys.argv[1])
            return density
        except ValueError:
            print("invalid density")
    return 4


def clear():
    subprocess.call('cls' if os.name == "nt" else 'clear')

def show_show_storm(row: int, column: int, density: int = 4):
    for y in range(row):
        for x in range(column):
            if random.randint(0, 99) < density:
                print(random.choice([TOP, BOTTOM]), end='')
            else: 
                print(' ', end='')
        print()

    print(f"{"\33[33m"}{FULL * column + '\n' + FULL * row}")
    time.sleep(0.323)

def main():
    clear()
    if len(sys.argv) == 1:
        density = set_desity()
        clear()
    else:
        density = set_density2()

    while True:
        try:
            show_show_storm(40, 40, density)
            clear()
        except KeyboardInterrupt:
            clear()
            print("key board interupt")
            return 0

if __name__ == "__main__":
    sys.exit(main())