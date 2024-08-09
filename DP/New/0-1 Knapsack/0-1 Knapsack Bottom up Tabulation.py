class Solution:
    
    # Function to return max value that can be put in knapsack of capacity maxWeight.
    def knapSack(self, maxWeight, wt, val, n):
        # Initialize the dp table with 0
        dp = [[0 for _ in range(maxWeight+1)] for x in range(n)]

        # dp[i][j] will store the maximum value that can be obtained
        # with the first i items and a knapsack capacity of j.
        # Value is rows and capacity is column
        
        # Base case for calculating the first row when we can choose only items[0]. 
        for c in range(maxWeight+1):
            if wt[0] <= c:
                dp[0][c] = val[0]


        # Process Bottom up
        for ind in range(1, n):    
            for w in range(maxWeight+1):
                
                no_take = 0 + dp[ind - 1][w]

                take = float("-inf")
                if wt[ind] <= w:
                    take = val[ind] + dp[ind - 1][w - wt[ind]]

                dp[ind][w] = max(take, no_take)
        # print(dp)
        return dp[n-1][maxWeight]
            
# Example usage
print(Solution().knapSack(maxWeight=8, wt=[5,2,3,1], val=[4,4,7,1], n=4))
print(Solution().knapSack(maxWeight=4, wt=[4,5,1], val=[1,2,3], n=3))
print(Solution().knapSack(maxWeight=7, wt=[1,2,4], val=[10,15,40], n=3))
