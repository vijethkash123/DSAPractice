import sys
lis=[2,3,2]
total=1
plist=[]
fnlist=[]
for i in lis:
    #print(i)
    total= total*(i+1)
ilen=len(lis)

print("Total->>"+str(total))

def rec(n):
    # fl=[]
    ol=[]
    print("Item->>"+str(lis[n-1]))
    it=total/(lis[n-1]+1)
    print("IT----"+str(it))
    for i in range(int(it)):
        for j in range(int(lis[n-1])+1):
            ol.append(j)
    # print(ol)
    return(ol)

#print(fl)

for i in range(len(lis)):
    plist.append(rec(i))

# for i in plist:
#     for j in range(len(i)):
#         fnlist.append([])
# print(plist)
print("\n\n\n\n")
print(plist)
#print(plist)
# sys.exit()
# print(plist[len(plist)-1])
# print(len(plist[0][0]))
# for i in range(len(plist[0][0])):
#     for j in plist:

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
print("FFN->>"+str(ffnlist))
