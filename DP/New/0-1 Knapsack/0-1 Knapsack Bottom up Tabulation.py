'''
knapSack -> General bottom up approach 2D array
knapSack_two_row -> Just using 2 single rows prev and cur instead of whole 2D array
knapSack_single_row -> Overwriting same prev row by iterating right to left n-1 to 0 and not making use of 2 rows cur and prev.
'''
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


    # Space optimized using single row -> SC is O(2.maxWeight + 1) == O(maxWeight)
    def knapSack_two_row(self, maxWeight, wt, val, n):
        prev = [0 for _ in range(maxWeight+1)]
        cur = [0 for x in range(maxWeight+1)]
        
        for c in range(maxWeight+1):
            if wt[0] <= c:
                prev[c] = val[0]


        # Process Bottom up
        for ind in range(1, n):    
            for w in range(maxWeight+1):
                
                no_take = 0 + prev[w]

                take = float("-inf")
                if wt[ind] <= w:
                    take = val[ind] + prev[w - wt[ind]]

                cur[w] = max(take, no_take)
            # print(prev)
            prev = cur[:]  # deepcopy is important to avoid errors
        
        return prev[maxWeight]


    # Space complexity: O(maxWeight) -> Here we overwrite the same prev and iterate from right to left instead of 0 to n. If we go from 0 to n we might overwrite some values that are required later for current row from previos row. So if we go from n-1 to 0, we will have the prev values as we find values at current index and also overwrite in same place.
    def knapSack_single_row(self, maxWeight, wt, val, n):
        prev = [0 for _ in range(maxWeight+1)]
        
        for c in range(maxWeight+1):
            if wt[0] <= c:
                prev[c] = val[0]


        # Process Bottom up
        for ind in range(1, n):    
            for w in range(maxWeight, -1, -1):
                
                no_take = 0 + prev[w]

                take = float("-inf")
                if wt[ind] <= w:
                    take = val[ind] + prev[w - wt[ind]]

                prev[w] = max(take, no_take)
            # print(prev)
        
        return prev[maxWeight]

# Example usage
print(Solution().knapSack(maxWeight=8, wt=[5,2,3,1], val=[4,4,7,1], n=4))
print(Solution().knapSack(maxWeight=4, wt=[4,5,1], val=[1,2,3], n=3))
print(Solution().knapSack(maxWeight=7, wt=[1,2,4], val=[10,15,40], n=3))


print(Solution().knapSack_two_row(maxWeight=8, wt=[5,2,3,1], val=[4,4,7,1], n=4))
print(Solution().knapSack_two_row(maxWeight=4, wt=[4,5,1], val=[1,2,3], n=3))
print(Solution().knapSack_two_row(maxWeight=7, wt=[1,2,4], val=[10,15,40], n=3))



print(Solution().knapSack_single_row(maxWeight=8, wt=[5,2,3,1], val=[4,4,7,1], n=4))
print(Solution().knapSack_single_row(maxWeight=4, wt=[4,5,1], val=[1,2,3], n=3))
print(Solution().knapSack_single_row(maxWeight=7, wt=[1,2,4], val=[10,15,40], n=3))