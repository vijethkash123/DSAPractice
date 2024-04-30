coins=[1,2,5]
amount=6

dp=[[float('inf') for i in range(amount+1)] for j in range(len(coins)+1)]
def min_coin(coins,amount):
    for i in range(len(coins)+1):
        for j in range(amount+1):
            if i==0:
                break
            if j==0:
                dp[i][j]=0
            elif coins[i-1] <=j:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(coins)][amount]

print(min_coin(coins,amount))
    