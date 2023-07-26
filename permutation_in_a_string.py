class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        s1d = {}
        s2d = {}
        for i in range(len(s1)):
            s1d[s1[i]] = 1 + s1d.get(s1[i], 0)
            s2d[s2[i]] = 1 + s2d.get(s2[i], 0)            
        
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if s1d == s2d:
                return True
            if s2d[s2[l]] == 1:
                s2d.pop(s2[l]) 
            else:
                s2d[s2[l]]-=1
            r+=1
            if r  > len(s2)-1:
                break
            s2d[s2[r]] = 1 + s2d.get(s2[r], 0)
            l+=1
        return False
        
obj = Solution()
print(obj.checkInclusion(
"ab",
"eidbaoaoo"))