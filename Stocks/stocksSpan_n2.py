stocks=[100, 80, 60, 70, 60, 75, 85]
n=len(stocks)

# ans=[1,1,1,2,1,4,6]
ss=[]
for i in range(n):
    count=0
    if i==0:
        ss.append(1)
    else:
        for j in range(i-1,0,-1):
            if stocks[j] > stocks[i]:
                break
            else:
                count+=1
        ss.append(count+1)
    
print(ss)

