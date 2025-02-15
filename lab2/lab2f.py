#!/usr/bin/env python3

import sys

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1 after each loop

print("blast off!")
