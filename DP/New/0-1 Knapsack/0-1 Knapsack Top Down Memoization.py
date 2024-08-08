class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        # Initialize the dp table with -1
        dp = [[-1 for _ in range(W+1)] for x in range(n+1)]
        # print(dp)
        
        # Recursive function with memoization
        def recur(ind, W):
            # Base case
            if ind == 0:
                if wt[0] <= W:  # if first item has lesser cost than remaining W, consider it else continue without considering it (returning 0)
                    return val[0]
                else:
                    return 0

            # Return the stored value if already computed
            if dp[ind][W] != -1:
                return dp[ind][W]
            
            # Case when the current item is not included
            no_take = 0 + recur(ind - 1, W)
            
            # Case when the current item is included
            take = float("-inf")
            if wt[ind] <= W:
                take = val[ind] + recur(ind - 1, W - wt[ind])
            
            # Store the result in the dp table
            dp[ind][W] = max(no_take, take)
            return dp[ind][W]

        # Start the recursion with the last item and full capacity
        return recur(n-1, W)
            
# Example usage
print(Solution().knapSack(W=4, wt=[4,5,1], val=[1,2,3], n=3))
