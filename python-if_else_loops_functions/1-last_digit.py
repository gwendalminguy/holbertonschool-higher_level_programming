#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0 & last != 0:
    last -= 10
if last == 0:
    end = "0"
elif last > 5:
    end = "greater than 5"
else:
    end = "less than 6 and not 0"
print(f"Last digit of {number} is {last} and is {end}")
