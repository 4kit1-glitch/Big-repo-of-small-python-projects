# a matrix screen saver 
# code is direct so i cant be explaining anything
import os
import sys
import subprocess
import random
import time

WIDTH = 70
GREEN = "\33[32m"
RESET = "\33[0m"
try: 
    subprocess.run("cls" if os.name == "nt" else "clear")
    columns = [0] * WIDTH

    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)
            if columns[i] == 0:
                print(" ", end='')
            else:
                print(f"{GREEN}{random.choice([0, 1])}{RESET}", end='')
                columns[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    print (f"{"\33c"}{"\33[34m"}kill program")
    sys.exit()