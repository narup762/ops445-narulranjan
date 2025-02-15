#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    timer = int(sys.argv[1])  # Convert the first argument to an integer
else:
    timer = 3  # Default value if no argument is provided

while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1 after each loop

print("blast off!")
