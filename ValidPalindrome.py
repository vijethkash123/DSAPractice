class Solution:
    def isalphanum(self, c):
        return (ord('A')<=ord(c)<=ord('Z')) or (ord('a')<=ord(c)<=ord('z')) or ord('0')<=ord(c)<=ord('9')

    def isPalindrome(self, s: str) -> bool:
        # Using Two pointer approach
        l = 0
        r = len(s)-1
        while l<r:
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
                continue
            elif not self.isalphanum(s[l]):
                l+=1
            elif not self.isalphanum(s[r]):
                r-=1
            else:
                return False
        return True

obj = Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))