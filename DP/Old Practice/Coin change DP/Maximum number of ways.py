n=5
table = [0 for i in range(0,n+1)]
table[0]=1
for i in range(1,n+1):
    table[i]+=table[i-1]
for i in range(2,n+1):
    table[i]+=table[i-2]
for i in range(5,n+1):
    table[i]+=table[i-5]
print(table[n])

#Example for overlapping subproblem in DP
#Similar to Volleyball score problem 