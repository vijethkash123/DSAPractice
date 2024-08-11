class Solution:

    # Top Down Memoization
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def dfs(i):
            if i == len(s):
                return 1

            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if ((i + 1 < len(s)) and int(s[i: i + 2]) <= 26):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)
    
    # Bottom Up DP
    def numDecodings_BU(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[len(s)] = 1  # C1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
        
                if ((i + 1 < len(s)) and int(s[i: i + 2]) <= 26):
                    dp[i] += dp[i + 2]

        # print(dp)
        return dp[0]


print(Solution().numDecodings(s="226"))  # 3
print(Solution().numDecodings(s="102"))  # [10, 2] is the only way, we can't decode leading zeroes at beginning, so ans is 1
print(Solution().numDecodings(s="660"))  # 0
print(Solution().numDecodings(s="066"))  # 0


print(Solution().numDecodings_BU(s="226"))  # 3
print(Solution().numDecodings_BU(s="102"))  # [10, 2] is the only way, we can't decode leading zeroes at beginning, so ans is 1
print(Solution().numDecodings_BU(s="660"))  # 0
print(Solution().numDecodings_BU(s="066"))  # 0