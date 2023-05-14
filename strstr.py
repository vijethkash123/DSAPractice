class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nH= len(haystack)
        nL = len(needle)

        # there is no need to iterate after length of hatstack gets smaller than needle
        begin = 0
        while nH-begin >= nL:
            i = 0
            while i<nL and needle[i] == haystack[i+begin]:
                i+=1
            if i == nL and needle == haystack[begin:i+begin]:
                return begin
            begin+=1
        return -1

obj = Solution()
print(obj.strStr("mississippi", "issippi"))
