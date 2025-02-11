#!/usr/bin/env python3
# Author ID: [mzaman30]

def is_digits(sobj):
    # Loop through each character in the string and check if it's a digit
    for char in sobj:
        if char not in '0123456789':  # Check if the character is not a digit
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
