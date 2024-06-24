from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(' ')

        trie = Trie()
        for d in dictionary:
            trie.insert(d)


        for i, w in enumerate(words):
            words[i] = trie.search(w)


        return ' '.join(words)
        

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:  # If character c is present in the Tree
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True  # After exiting the for loop, when we are at the last letter of the word

    def search(self, word: str) -> bool:
        cur = self.root
        prefix = ""
        for c in word:
            if c not in cur.children:
                return word
            cur = cur.children[c]
            prefix += c

            if cur.endOfWord:
                return prefix
        return word



print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))