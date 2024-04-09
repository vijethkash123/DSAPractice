from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ni, nj = len(board), len(board[0])
        visited = set()  # To keep track of visisted cell [i,j]

        def dfs(i, j, cur):
            if cur == len(word):  # If i has reached to length of word without getting False on below conditions, then we have a match
                return True
            if (
                (i >= ni or j >= nj)
                or (i < 0 or j < 0)
                or ((i, j) in visited)  # donot visit the cell that is already visited in the DFS call
                or (word[cur] != board[i][j])  # letter in subset not equal to letter in word
            ):
                return False
            visited.add((i, j))
            return dfs(i - 1, j, cur+1) or dfs(i + 1, j, cur+1) or dfs(i, j - 1, cur+1) or dfs(i, j + 1, cur+1)
            visited.remove((i, j))

        for i in range(ni):
            for j in range(nj):
                if dfs(i, j, 0):
                    return True
        return False


print(
    Solution().exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
