from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        # self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:  # If character c is present in the Tree
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # cur.endOfWord = True  # After exiting the for loop, when we are at the last letter of the word

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = []
        trie = Trie()
        for i in range(1, n + 1):
            # insert into Trie
            trie.insert(str(i))
        # print(trie.root.children['1'].children)  # to see tries
        # print(trie.root.children['2'].endOfWord)  # to see 2 has end of word

        # Do DFS and print get all values in Trie, you get it in lexicographical order
        res = []
        def dfs(cur, subset):
            if not cur.children:
                return
            for c in cur.children:  # cur.children is a dictionary. each has a TrieNode as value. See ex1 below
                res.append(subset + c)
                dfs(cur.children[c],  subset + c)
            return res
        
        return dfs(trie.root, "")


print(Solution().lexicalOrder(n = 13))



'''
ex1:
{
'0': <__main__.TrieNode object at 0x00000222B70143D0>, 
'1': <__main__.TrieNode object at 0x00000222B7014450>, 
'2': <__main__.TrieNode object at 0x00000222B70144D0>, 
'3': <__main__.TrieNode object at 0x00000222B7014550>
}
'''