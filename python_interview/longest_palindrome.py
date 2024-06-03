def longest_palindrome(s):
    if s == '':
        return ''
    
    counts = {}
    # populate counts dictionary
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    
    longest_palindrome_length = 0
    found_odd = False
    
    for _, count in counts.items():
        if count % 2 == 0:
            longest_palindrome_length += count
        else:
            found_odd = True
            longest_palindrome_length += count - 1
    
    if found_odd:
        longest_palindrome_length += 1
    
    return longest_palindrome_length

# Test cases
print(longest_palindrome('abccccdd')) # 7
print(longest_palindrome('a')) # 1
print(longest_palindrome('bb')) # 2
print(longest_palindrome('')) # 0
print(longest_palindrome('racecar')) # 7