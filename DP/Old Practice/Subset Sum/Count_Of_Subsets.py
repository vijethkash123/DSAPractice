set = [1, 2,3,3]
sum = 6

dp=[[0 for i in range(sum+1)] for j in range(len(set)+1)]

def SS(set,sum):
    for i in range(len(set)+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1 #Here dp[0][0] will be overwritten to 1
            elif set[i-1] <=j:
                dp[i][j]= dp[i-1][j] + dp[i-1][j-set[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp

print(SS(set,sum))