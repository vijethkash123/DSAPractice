set = [1, 3, 2, 5, 4, 9]
sum = 11

dp=[[False for i in range(sum+1)] for j in range(len(set)+1)]

def SS(set,sum):
    for i in range(len(set)+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]=False 
            if j==0:
                dp[i][j]=True #Here dp[0][0] will be overwritten to True
            elif set[i-1] <=j:
                dp[i][j]= dp[i-1][j] or dp[i-1][j-set[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(set)][sum]

print(SS(set,sum))