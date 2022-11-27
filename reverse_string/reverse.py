'''
Given a string, reverse its output
'''

def reverse_string(string):

    # subtract one as len doesn't account for 0 index
    length = len(string) - 1
    new_string = ""

    # loop through string backwards and add to new string
    for i in range(length, -1, -1):
        new_string = new_string + string[i]
    
    return new_string
