# Write a program to know if the number is prime or not

def prime_number(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
      
# Input: v4h5j2
# Ouput : vvvvhhhhhjj
# Write a python code for the above problem
def decode_string(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i] * int(s[i+1])
    return result

s = "v4h5j2"
print(decode_string(s))


# Given two dates, write a program to find the number of business days that exist between the date range.

# date1 = 2021-01-31
# date2 = 2021-02-18
# Output: 14
from datetime import datetime, timedelta

def delta_buss_days(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")
    delta = date2 - date1
    buss_days = 0
    for i in range(delta.days + 1):
        if (date1 + timedelta(days=i)).weekday() < 5:
            buss_days += 1
    return buss_days

print(business_days("2021-01-31", "2021-02-18"))



# Write a function that should output a centred triangle shape 
# made up of the desired symbol. The number of symbols in each 
# row should increase by two with each level, starting with one 
# symbol on the first level, then three on the second level and 
# so on until the final level is reached

def print_triangle(n, symbol):
    for i in range(1, n+1):
        print(" " * (n-i) + symbol * (2*i - 1))
        
# Flatten a nested list [1, [2, [3, 4], 5], 6, [7, 8]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]

def flatten_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

# Group consectutive elements 
# Input: [1, 2, 3, 5, 6, 7, 9, 10]
# Output: [(1,2,3), (5,6,7), (9,10)]
def consecutive_elements(lst):
    result = []
    temp = []
    for i in lst:
        if not temp or i == temp[-1] + 1:
            temp.append(i)
        else:
            result.append(tuple(temp))
            temp = [i]
    result.append(tuple(temp))
    return result

def consecutive_chars_in_string(s):
    result = []
    temp = []
    for i in s:
        if not temp or i == temp[-1] + 1:
            temp.append(i)
        else:
            result.append("".join(temp))
            temp = [i]
    result.append("".join(temp))
    return result

def consecutive_dates(dates):
    result = []
    temp = []
    for i in range(len(dates)):
        if not temp or dates[i] == dates[i-1] + timedelta(days=1):
            temp.append(dates[i])
        else:
            result.append(tuple(temp))
            temp = [dates[i]]
    result.append(tuple(temp))
    return result

# Find all pairs that sum to a target 6
# Input: [1, 2, 3, 4, 5]
# Output: [(1, 5), (2, 4)]
def find_pairs(lst, target):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                result.append((lst[i], lst[j]))
    return result

