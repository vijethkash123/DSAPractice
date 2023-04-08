a=[1,1,2,3,2,5,2,2,2,3,3,3]
ddict={}
for i in a:
    if i not in ddict:
        ddict[i]=1
    else:
        ddict[i]=ddict[i]+1

print(ddict)
print("\n")
for i,j in ddict.items():
    if j%2==0:
        print("We have "+str(int(j/2))+" pairs of "+str(i))
    else:
        print("We have "+str(int(j-1)/2)+" pairs of "+str(i))
