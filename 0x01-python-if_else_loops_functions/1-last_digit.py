#!/usr/binpython3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number[-1], end="")
if number[-1] > 5:
    print(" and is greater than 5")
elif number[-1] == 0:
    print(" and is zero")
else:
    print(" and is less than 6 and not 0")
