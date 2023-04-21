class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or len(needle) > len(haystack):
            return -1

        l = 0
        r = 1
        while l < len(haystack) and r <= len(haystack):
            if r-l == len(needle) and haystack[l:r] == needle:
                return l
            if haystack[l] != needle[0]:
                l += 1
                r = l+1
            else:
                if r < len(haystack) and haystack[r] == needle[r-l]:
                    r+=1
                else:
                    l = l+1
                    r = l+1
        return -1

obj = Solution()
print(obj.strStr("mississippi", "issipi"))
