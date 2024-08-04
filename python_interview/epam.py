"""
You are given an array of N of integers. You want to split them into N/2 pairs in such a way that the sum of integers in each pair is odd. N is even and every element of the array must be present in exactly one pair. 
Your task is to determine whether it is possible to split the numbers into such pairs. For example, given [2, 7, 4, 6, 3, 1], the answer is True. One of the possible sets of pairs is (2,7), (6,3), and (4,1). their sums are respectively 9,9, and 5, all of which are odd. 

Write a function which, given array of integers A of length N, returns True when it is possible to create the required pairs and False otherwise. 
"""

def solution(A):
    odd = 0
    even = 0
    for i in A:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd == even

# Test cases
print(solution([2, 7, 4, 6, 3, 1])) # True
print(solution([-1, 1]))
print(solution([2, -1]))
print(solution([1, 2, 3, 4]))
print(solution([-1, -3, 4, 7, 7, 7]))