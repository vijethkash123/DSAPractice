from functools import reduce
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        strs = list(map(lambda x:str(len(x))+"#"+x, strs))
        s = reduce(lambda x,y: x+y, strs)
        return s
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        res = []
        num = ""
        i = 0
        while i<len(s):
            if s[i].isnumeric():
                num+=str(s[i])
                i+=1
                continue
            if s[i]=="#":
                res.append(s[i+1:i+int(num)+1])
                i = i+int(num)+1
                num=""

        return res

obj = Solution()
inputD = ["lint","code","love","you"]

res = obj.encode(inputD)
print(res)
print(obj.decode(res))
