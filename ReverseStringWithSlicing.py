"""
Reversing string with Slicing Operation
"""

def reverse_string(s):
    return s[::-1]

# Test the function
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f'Reversed string: {reversed_string}')
