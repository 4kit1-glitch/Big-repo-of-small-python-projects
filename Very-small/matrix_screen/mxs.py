import sys
import random
import time

WIDTH = 70
GREEN = "\33[32m"
RESET = "\33[0m"
try: 
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
    sys.exit()