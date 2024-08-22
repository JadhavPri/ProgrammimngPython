"""
Find largest and second largest number
"""

def find_largest_and_second_largest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements.")

    # Initialize the largest and second largest
    largest = second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    if second_largest == float('-inf'):
        raise ValueError("No second largest element found (all elements might be the same).")

    return largest, second_largest


# Example usage:
nums = [10, 4, 6, 7, 10, 5]
largest, second_largest = find_largest_and_second_largest(nums)
print("Largest:", largest)
print("Second Largest:", second_largest)




