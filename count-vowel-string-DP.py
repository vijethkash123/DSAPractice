class Solution(object):
    def countVowelStrings(self, n):   
        dp=[[-1 for i in range(5)] for j in range(n+1)] #5 because a e i o u
        result = self.solve(n,0,dp)
        print(dp[n][0])
        return result
    
    def solve(self,n,lastVowel,dp):
        if(dp[n][lastVowel]==-1):  #Unsolved, Cache miss
            if(n==0):
                dp[n][lastVowel] = 1
            else:
                result=0
                for i in range(lastVowel,5):
                    result+=self.solve(n-1,i,dp)
                dp[n][lastVowel]=result  #Update the table after computing result
                
        return dp[n][lastVowel] #If already solved directly return, Cache hit

if __name__ == "__main__":
    obj=Solution()
    print(obj.countVowelStrings(2))