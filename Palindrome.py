"""
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization. 
For example, "racecar" and "level" are palindromes because they spell the same thing in both directions. 
In phrases or sentences, spaces and punctuation are often ignored, so "A man, a plan, a canal, Panama!" is also a palindrome.

"""

"""
1. Take a string from the user
2. Write a function to check if the string is a palindrome
   a) Initialize an empty list to store characters
   b) For each Loop through each character in the input string
       i ) Chekc if it's alphanumeric 
       ii ) If yes, convert to lowercase and append to the empty list
   c) Join the filtered list into a single cleaned string
   d) Check if the cleaned string reads the same forwards and backwards
3. Create an if-else statement to call the function & print true result in if block & false result in else block

Note: 

-- ''.join(filtered_chars) --> Converts List to a string e.g. ['a', 'b', 'c', 'd'] = abcd 
--  isalnum() is an inbuilt method in Python. It is a string method that checks if all the characters in a given string are alphanumeric. An alphanumeric character is either a letter (a-z, A-Z) or a digit (0-9).

"""

def is_palindrome(s):
    # Initialize an empty list to store characters
    filtered_chars = []

    # Loop through each character in the input string
    for c in s:
        # Check if the character is alphanumeric
        if c.isalnum():
            # Convert to lowercase and append to the list
            filtered_chars.append(c.lower())

    # Join the list into a single cleaned string
    cleaned_string = ''.join(filtered_chars)

    # Check if the cleaned string reads the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]


# Test the function
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
