set = [1,3,2,2,4]
sum = 4

# set=[1,2,3,3]
# sum=6

# set = [5, 10, 12, 13, 15, 18]
# sum=30

set = [1,2,3]
sum = 4

dp=[[False for i in range(sum+1)] for j in range(len(set)+1)]


def SS(set,sum):
    n=len(set)
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
    p=[]
    for i in range(len(dp)):
        print(dp[i])
        print("\n")
    # for i in range(n,0,-1):
    #     p=[]
    pss(set,n,sum,p)
    
def pss(set,i,sum,p):
    if i==0 and sum!=0:
        # p=[]
        return
    if sum==0:
        # p.append(set[i])
        print(p)
        p=[]
        return
    if sum<0:
        return

    if dp[i-1][sum]:
        b=[]
        b.extend(p)
        pss(set,i-1,sum,b)

    # print(dp[i][sum],i,sum)
    if dp[i][sum]:
        p.append(set[i-1])
        # print(p)
        pss(set,i-1,sum-set[i-1],p)
    else:
        return
    
    # if i==0 and sum!=0 and dp[0][sum]:
    #     p.append(set[i])
    #     print(p)
    #     p=[]
    #     return
    #Explanation:
    #for [3,1], after we get 3, and then we traverse dp[3][1]-- True , dp[2][1]--True, dp[1][1]-- True untill dp[i-1][sum] becomes False -- dp[0][1] False


SS(set,sum)