"""
Given a list, write a function encode which one-hot encodes the items in the list. When one-hot encoding, the most significant bit (index zero) should be represented by the first unique element in the list.

Example1:
Input:
elements = [1, 3, 4, 3, 2, 1]

Output:
def encode(elements) -> [[1, 0, 0, 0], [0, 1, 0, 0],
 [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
 
Example2:
Input:
elements = ['hi', 'hello', 'amazing', 'amazing']

Output:
def encode(elements) -> [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]]
"""

def encode(elements):
    one_hot = []
    unique_elements = list(set(elements))
    for element in elements:
        one_hot.append([1 if element == unique_element else 0 
                        for unique_element in unique_elements])
    return one_hot

elements = [1, 3, 4, 3, 2, 1]
print(encode(elements))
