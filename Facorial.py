"""
In mathematics, the factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted by n!

5!=5×4×3×2×1=120

"""

"""
1. Take the input in integer format
2. Define a function to check if it's a factorial
   a) Check if given int is less than zero & print a message fact not defined
   b) initialize a variable to 1 for result variable
   c) For each loop using range function to run from 1 to 5 
   d) Return result
   
"""
def factorial(n):
    # Check if the input is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers."

    # Initialize the result to 1 (factorial of 0 is 1)
    result = 1

    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Multiply result by the current number
        result *= i

    return result


# Test the function
input_number = int(input("Enter a number to compute its factorial: "))
factorial_result = factorial(input_number)
print(f'The factorial of {input_number} is {factorial_result}.')
