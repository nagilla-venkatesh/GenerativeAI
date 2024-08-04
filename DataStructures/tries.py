"""
A trie also called prefix-tree, is a type of search tree, a tree 
data structure used for locating specific keys from within a set.
These keys are always strings and characters are stored at each node.
A trie node is structured by trie nodes. 
Each trie node has two components:
1. A set of childern that leads to the next trie node, and 
2. A boolean value defines if it the end of the word.
--------------------------------------------------------------------
Applications:

1. Auto-complete
2. Spell checker
3. Solving boogle games 
"""

import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        """Initialize your data structure here.
        """
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        content = self.root
        for letter in word:
            content = content.children[letter]
        content.end_of_word = True
        
    def search(self, word: str) -> bool:
        content = self.root
        for letter in word:
            content = content.children.get(letter)
            if content is None:
                return False
        return content.end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        content = self.root
        for letter in prefix:
            content = content.children.get(letter)
            if content is None:
                return False
        return True


# Test the Trie
trie = Trie()
trie.insert("apple")
print(trie.search("apple")) # True
print(trie.search("app")) # False
print(trie.startsWith("app")) # True
trie.insert("app")
print(trie.search("app")) # True
