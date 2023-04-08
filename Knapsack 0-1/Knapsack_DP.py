def KS(weights,values,capacity,n):
    dp=[[0 for i in range(capacity+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for c in range(capacity+1):
            if i==0 or c==0:
                dp[i][c]=0
            elif weights[i-1]<=c:
                dp[i][c]=max(values[i-1]+dp[i-1][c-weights[i-1]],dp[i-1][c])
            else:
                dp[i][c]=dp[i-1][c]
    return dp[n][capacity]

# print(KS([10, 40, 50, 70],[1, 3, 4, 5],8,4))
print(KS([1,50],[1, 30],100,2))


