import sys
s="aabc"
s1="skjdjaabcooppe"
# count=[0]*len(s)
count={}

for i in s:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
for j in range(0,len(s1)):
    count1={}
    temp=s1[j:len(s)+j]
    # print(temp)
    for i in temp:
        if i not in count1:
            count1[i]=1
        else:
            count1[i]+=1
    if  count1==count:
        # print(count1,count)
        print(True)
        sys.exit()
    else:
        continue
print(False)

