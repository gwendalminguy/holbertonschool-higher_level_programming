#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    bis = -number
else:
    bis = number
last = bis % 10
if last == 0:
    end = "0"
elif last > 5:
    end = "greater than 5"
else:
    end = "less than 6 and not 0"
print(f"The last digit of {number} is {last} and is {end}")
