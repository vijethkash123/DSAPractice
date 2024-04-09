from typing import *

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i+3, len(s))):  # to get around the index out of range error
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):  # C1
                    dfs(j+1, dots+1, curIP+s[i:j+1]+".")

        dfs(0, 0, "")
        return res
    
print(Solution().restoreIpAddresses("25525511135"))