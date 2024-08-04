input = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = [["bat"], ["nat", "tan"], ["eat", "ate", "tea"]]
 
from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())

output = group_anagrams(input)
print(output)
