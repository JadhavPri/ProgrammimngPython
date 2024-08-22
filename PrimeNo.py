"""
Prime no : 

 -- If a number n is only divisible by 1 and itself, it will have no divisors other than 1 and itself up to its square root. 
 -- Thus, it is considered a prime number.
 -- Prime numbers are defined as positive integers greater than 1. Hence, any number less than or equal to 1 (including negative numbers and zero) cannot be prime.
 -- 2 and 3 are prime numbers. Any number divisible by 2 or 3 is not a prime (except 2 and 3 themselves). 

 Non-Prime no:

 -- Non-Prime Number: If n is divisible by any number up to its square root, it will have factors in pairs where one factor is less than or equal to the square root and the other is greater than or equal to the square root. 
 -- This means n is not a prime number.


Example:
Example 1: 29

The square root of 29 is approximately 5.39.
Check divisors up to 5 (2, 3, 5):
29 is not divisible by 2, 3, or 5.
Therefore, 29 is a prime number.
Example 2: 30

The square root of 30 is approximately 5.47.
Check divisors up to 5:
30 is divisible by 2, 3, and 5.
Since 30 has divisors other than 1 and itself, it is not a prime number.

"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
number = int(input("Enter a number to check if it's prime: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
