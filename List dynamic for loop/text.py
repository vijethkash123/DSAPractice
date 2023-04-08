lis=[2,3,2,4]
def rec(n):
  for i in range(lis[n]+1):
    print(i)
print("llllll"+str(len(lis)))
for i in range(len(lis)):
  rec(i)