set = [1,5,6,11]
sum=0
firstSumPartition=0
secondSumPartition=0
min_difference=0
for i in range(len(set)):
    sum = sum+set[i]

total=sum

sum=sum/2

def SS(set,sum):
    dp=[[False for i in range(sum+1)] for j in range(len(set)+1)]
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
    return dp

dp = SS(set,sum)

for i in range(sum,0,-1):
    if dp[len(set)][i]==True:
        firstSumPartition=i
        break
# print(firstSumPartition)

secondSumPartition = total - firstSumPartition

min_difference = secondSumPartition-firstSumPartition

print(min_difference)