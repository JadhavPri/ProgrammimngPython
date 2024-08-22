"""
Reverse a string with Recursion

"""

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Test the function
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print(f'Reversed string: {reversed_string}')


"""
How recursion works

Explanation with "hey"
Initial Call: reverse_string("hey")

s = "hey"
Check: len("hey") is 3, not 0, so move to the recursive case.
Recursive Call: reverse_string("ey") (sliced s[1:]) + "h"
Recursive Call: reverse_string("ey")

s = "ey"
Check: len("ey") is 2, not 0, so move to the recursive case.
Recursive Call: reverse_string("y") (sliced s[1:]) + "e"
Recursive Call: reverse_string("y")

s = "y"
Check: len("y") is 1, not 0, so move to the recursive case.
Recursive Call: reverse_string("") (sliced s[1:]) + "y"
Base Case: reverse_string("")

s = ""
Check: len("") is 0, so return "" (empty string).
Combining Results
Now let's combine the results from the recursive calls:

Base Case: reverse_string("") returns ""

Recursive Call reverse_string("y"):

Returns: "" + "y" → "y"
Recursive Call reverse_string("ey"):

Returns: "y" + "e" → "ye"
Initial Call reverse_string("hey"):

Returns: "ye" + "h" → "yeh"
Step-by-Step Breakdown
Initial Call: reverse_string("hey")

Slices "hey" to "ey" and appends "h".
Second Call: reverse_string("ey")

Slices "ey" to "y" and appends "e".
Third Call: reverse_string("y")

Slices "y" to "" (empty string) and appends "y".
Base Case: reverse_string("")

Returns "".
Summary
Each Call: Reduces the string by removing the first character and then processes the remaining substring.
Base Case: Stops recursion when the string is empty.
Combining Results: Each recursive call builds the reversed string by appending the first character of the current substring to the reversed result of the remaining substring.
Thus, the function reverse_string("hey") eventually returns "yeh" as the reversed string.

"""
