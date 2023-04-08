import math
import os
import random
import re
import sys

#easy solution down
# s, n = input().strip(), int(input().strip())
# print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
def repeatedString(s, n):
    ls=len(s)
    i=0
    ac=0
    for i in s:
        if i=='a':
            ac+=1
    if ac==0:
        return 0
    q=int(n/ls)*ac
    rm = n %ls
    ans=0
    if rm == 0 :
        return q
    else:
        s=s[:rm]
        for i in s:
            if i=='a':
                ans+=1
        ans=ans+q
        return ans
        # ans=q+ac
        # return ans


if __name__ == '__main__':

    s="aba"
    n=10
    result = repeatedString(s, n)
    print(result)
