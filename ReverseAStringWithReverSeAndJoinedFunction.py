"""
-- reversed(s) returns an iterator that yields characters from s in reverse order.
-- ''.join(reversed(s)) joins these characters into a new string.

"""

def reverse_string(s):
    return ''.join(reversed(s))

# Test the function
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f'Reversed string: {reversed_string}')
