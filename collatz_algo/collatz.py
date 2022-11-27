'''
Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''

def collatz_algo(starting):
    
    # Case 1: The number is less than or equal to 1
    if starting <= 1:
        return "The number has to be greater than 1"

    else:
        # steps counter
        steps = 0

        # loop through till number is 1
        while starting != 1:
            
            # if the number is even
            if starting % 2 == 0:
                starting /= 2
            
            # if the number is odd:
            else:
                starting = starting * 3 + 1
            
            steps += 1
    
    return steps






