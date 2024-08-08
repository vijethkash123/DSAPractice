class Solution:
    
    # Function to return max value that can be put in knapsack of capacity maxWeight.
    def knapSack(self, maxWeight, wt, val, n):
        # Initialize the dp table with 0. dp[i][j] will store the maximum value that can be obtained
        # with the first i items and a knapsack capacity of j.
        dp = [[0 for _ in range(maxWeight + 1)] for _ in range(n + 1)]

        # Iterate over each item
        for ind in range(1, n + 1):
            # Iterate over each capacity from 0 to maxWeight
            for w in range(maxWeight + 1):
                # Case when the current item is not included
                no_take = dp[ind - 1][w]
                
                # Case when the current item is included
                take = float("-inf")
                if wt[ind - 1] <= w:
                    take = val[ind - 1] + dp[ind - 1][w - wt[ind - 1]]
                
                # Store the maximum value obtained by including or not including the current item
                dp[ind][w] = max(take, no_take)

        # The answer is the maximum value that can be obtained with all n items and capacity maxWeight
        return dp[n][maxWeight]
            
# Example usage
print(Solution().knapSack(maxWeight=4, wt=[4, 5, 1], val=[1, 2, 3], n=3))
