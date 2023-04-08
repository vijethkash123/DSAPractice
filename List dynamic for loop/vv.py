import sys
lis=[2,3,2, 0]
total=1
plist=[]
fnlist=[]
for i in lis:
    total= total*(i+1)
ilen=len(lis)

print("Total->>"+str(total))

def rec(n):
    ol=[]
    it=1
    n1=n
    while n1 < (len(lis)-1):
        it=(lis[n1+1]+1)*it
        n1=n1+1
    print("IT->> "+str(it))
    x=int(int(total)/(int(it)))
    print("X->> "+str(x))
    for k in range(x):
        for m in range(lis[n]+1):
            for j in range(it):
                ol.append(m)
    ol=ol[:total]
    return(ol)

for i in range(len(lis)):
    plist.append(rec(i))

print(*plist,sep='\n\n\n')
# sys.exit()
len1=len(plist)
len2=len(plist[0])


# print(len1,len2)
ffnlist=[]
for i in range(len2):
    for j in range(len1):
        # print("I & J "+str(i)+str(j))
        fnlist.insert(j,plist[j][i])
    ffnlist.append(fnlist)
    fnlist=[]

print("\n\n")
# ffnlist=ffnlist[:total]
# print("FFN->>"+str(ffnlist))
print(*ffnlist,sep='\n')