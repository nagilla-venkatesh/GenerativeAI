"""
Given a list of integers, find the index at which the sum of the left half of the list is equal to the right half. If there is no index where this condition is satisfied return -1.

Note: the number that lies on the index is calculated to the left side of the list.

Example 1:

Input:

nums = [1, 7, 3, 5, 6]
Output:

equivalent_index(nums) -> 2
In this example, the sum of the elements to the left of index 2 (1 + 7) is equal to the sum of the elements to the right of index 2 (5 + 6).
"""

def equivalent_index(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i:]):
            return i - 1
    return -1

nums = [1, 7, 3, 5, 6]
print(equivalent_index(nums))

# Output: 2
nums = [1,3,5]
print(equivalent_index(nums))