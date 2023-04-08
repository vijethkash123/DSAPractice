sl=0 #sealevel
vc=0 #valley count
s="UDDDUDUU"
n=len(s)
print(n)
for i in s:
    if i == 'U':
        sl+=1
        if sl==0:
            vc+=1
    if i== 'D':
        sl-=1
print(vc)