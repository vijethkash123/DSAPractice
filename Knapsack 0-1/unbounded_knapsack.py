def KS(weights,values,capacity,n):
    dp=[[0 for i in range(capacity+1)] for i in range(n+1)]
    
    for i in range(n+1):
        for c in range(capacity+1):
            if i==0 or c==0:
                dp[i][c]=0
            elif weights[i-1]<=c:
                dp[i][c]=max(values[i-1]+dp[i][c-weights[i-1]],dp[i-1][c])
            else:
                dp[i][c]=dp[i-1][c]
    return dp[n][capacity]

print(KS([1,50],[1, 30],100,2))

#Output is 100 because 100 weight made from 1 gives 100 > 2 weights of 50 which gives 60