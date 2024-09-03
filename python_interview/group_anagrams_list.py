# Write a python code to group anagrams from a list of strings.

# input = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output = [["bat"], ["nat", "tan"], ["eat", "ate", "tea"]]

def group_anagrams(input):
    anagrams = {}
    for word in input:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input)
print(output)