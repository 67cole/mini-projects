'''
Program asks user how many decimal places to generate PI up to.
Uses Math library, so only a 15 number limit
'''

import math

def pi_to_dec(decimal):

    # Set variables
    pie = str(math.pi)
    num = ""

    # Case 1: If inputted number is larger than 15
    if decimal > 15:
        num = "Sorry! This program only offers up to 15 decimal places."

    # Case 2: A negative number is inputted
    elif decimal < 0:
        num = "You've entered a number smaller than 0. This is invalid!"

    # Case 3: If inputted number is 0
    elif decimal == 0:
        num = "3"

    # Case 4: A valid number is inputted
    else:
        # Decimal places start after 2 characters of '3' and '.'
        decimal += 2

        # Loop through the Pi string and add to string
        for i in range(0, decimal):
            num = num + pie[i]
    

    return num
