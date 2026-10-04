import time
from itertools import cycle

lights = [
    ("GREEN", 2),
    ("YELLOW", 0.5),
    ("RED", 2)
]

colours = cycle(lights)

while True:
    c, s = next(colours)
    print(c)
    time.sleep(s)
    