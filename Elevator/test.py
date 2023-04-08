lineList = list()
with open("input.txt") as f:
 for line in f:
    lineList.append(line)
lineList = [line.rstrip('\n') for line in open("input.txt")]
print(lineList)

VF=True
d_list=[]
f_list=[]
t_tup=()
for i in lineList:
    t_tup=(i[0],i[2])
    f_list.append(t_tup)
    d_list.append(i[1])
print(d_list)
print(f_list)

if d_list[0]==d_list[1]:
    VF=True
else:
    VF=False
print(VF)

if VF==True:
    print(str(f_list[0][0])+"---->"+str(f_list[1][0]))
    print("\n"+str(f_list[1][0])+"---->"+str(f_list[1][1]))
    print("\n"+str(f_list[1][1])+"---->"+str(f_list[0][1]))
else:
    print(str(f_list[0][0])+"---->"+str(f_list[0][1]))
    print("\n"+str(f_list[1][0])+"---->"+str(f_list[1][1]))