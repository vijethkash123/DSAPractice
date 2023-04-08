x="AGGTAB"
y="GXTXAYB"
n=len(x)
m=len(y)

# dp=[[None]*(m+1) for i in xrange(n+1)] 

dp=[[0 for i in range(m+1)] for j in range(n+1)]

def LCS_DP(x,y,n,m):
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][m]

print(LCS_DP(x,y,n,m))