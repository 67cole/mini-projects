'''
Checks if the string entered by the user is a palindrome. 
That is that it reads the same forwards as backwards like “racecar”
'''

def palindrome_check(word):

    # subtract one to length as it doesn't account for 0 index
    length = len(word) - 1

    # now loop through and check if each letter is equal, condition is that if the two pointers cross in the word
    i = 0
    while (i < length):
        
        # if they are not equal, return
        if word[i] != word[length]:
            return "This string is not a palindrome"
        
        i += 1
        length -= 1
    
    # if the while loop finishes, it's a palindrome
    return "It's a palindrome!"


