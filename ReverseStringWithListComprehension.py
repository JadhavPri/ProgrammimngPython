"""
Reverse a string with List Comprehension

"""
def reverse_string(s):
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])

# Test the function
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f'Reversed string: {reversed_string}')
