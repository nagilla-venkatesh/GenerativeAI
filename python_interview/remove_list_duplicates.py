# Remove duplicates from the list in python without using set 

def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst

lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(remove_duplicates(lst)) # [1, 2, 3, 4, 5]

from collections import OrderedDict

def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(remove_duplicates(lst)) # [1, 2, 3, 4, 5]

def consecutive_identical_elements(lst):
    return [lst[i] for i in range(len(lst)) 
            if i == 0 or lst[i] != lst[i - 1]]
    
test_list = [4, 5, 5, 5, 5, 6, 6, 7, 8, 2, 2, 10]
print(consecutive_identical_elements(test_list)) # [4, 5, 6, 7, 8, 2, 10]

def largest_number(lst):
    largest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
    return largest

nums = [10, 5, 8, 20, 3]
print(largest_number(nums)) # 20

def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

lst = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(count_frequency(lst)) # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2}

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_common_elements(lst1, lst2):
    return [value for value in lst1 if value in lst2]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2)) # [4, 5]

def find_second_largest(numbers):
    largest = second_largest = float('-inf')
    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number
    return second_largest

print(find_second_largest([10, 20, 4, 45, 99])) # 45

def remove_consecutive_duplicates(lst):
    return [v for i, v in enumerate(lst) if i == 0 or v != lst[i - 1]]

print(f'remove consectutive duplciates {remove_consecutive_duplicates([1, 2, 2, 3, 4, 4, 5])}') # [1, 2, 3, 4, 5]

def count_number_of_occurrences():
    from collections import Counter
    values = 'a','a','b','b','c','c','c','d','e'
    return Counter(values)

print(count_number_of_occurrences()) # Counter({1: 2, 2: 2, 3: 2, 4: 2, 5: 2})
    
def max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0
    for i in arr:
        current_sum = max(0, current_sum + i)
        max_sum = max(max_sum, current_sum)
    return max_sum

print(max_subarray_sum([1,2,3,-2,5])) # 9

def remove_punctuation(s):
    import string
    return s.translate(str.maketrans('', '', string.punctuation))

print(remove_punctuation('Hello, World!')) # Hello World

def uncommon_words(s1, s2):
    s1 = s1.split()
    s2 = s2.split()
    return set(s1).symmetric_difference(set(s2))

print(uncommon_words('apple banana mango', 'banana fruits mango')) # {'apple', 'fruits'}

def palindrome(s1, s2):
    return s1 == s1[::-1] and s2 == s2[::-1]

print(f'palindrome is {palindrome("madam", "madam")}') # True
