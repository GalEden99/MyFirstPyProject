# Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places.
# Keep a limit to how far the program will go.

import math

nth_digit = int(input("Enter how mach Pi digits do you want to see in range 1-5: "))
if 1 > nth_digit or nth_digit >= 6:
    print("You need to input an int between 1-5!")
else:
    nth_digit += 1

if nth_digit in range(7):
    print(str(math.pi)[:nth_digit])
