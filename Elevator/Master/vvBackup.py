import sys
class elevator:
    lineList = list()
    up_list=[]
    down_list=[]
    temp_l=[]

    with open("input.txt") as f:
        for line in f:
            lineList.append(line)
        lineList = [line.rstrip('\n') for line in open("input.txt")]
        print(lineList)
    
    for i in lineList:
        if i=='' or (str(i[1])=="u" and i[0]>i[2]) or (str(i[1])=="d" and i[0]<i[2]):
            continue
        else:
            temp_l.append(i)
        
    lineList=temp_l
    # print(temp_l)

    for i in lineList:
        if i[1]=="d":
            down_list.append(i)
        else:
            up_list.append(i)
    print(up_list)
    print(down_list)

    if str(lineList[0][1])=="u":
        print("\n\n"+"------------------------------------")
        for i in up_list:
            if int(up_list[0][2])>int(i[0]):
                print(str(i[0])+"is picked")
        temp_list=[]
        for i in up_list:
            temp_list.append(i[0])
            temp_list.append(i[2])
        #Sort and Unique logic 
        temp_list.sort()
        temp_list=set(temp_list)
        temp_list=list(temp_list)
        temp_list.sort()
        print("\n\n"+"------------------------------------")
        print("Lift going up in order -->")
        print(*temp_list,sep='\n')

        print("\n\n"+"------------------------------------")
        for i in down_list:
            if int(down_list[0][2])<int(i[0]):
                print(str(i[0])+"is picked")
        temp_list=[]
        for i in down_list:
            temp_list.append(i[0])
            temp_list.append(i[2])

        temp_list.sort()
        temp_list=set(temp_list)
        temp_list=list(temp_list)
        temp_list.sort()
        temp_list.reverse()
        print("\n\n"+"------------------------------------")
        print("Lift going down in order -->")
        print(*temp_list,sep='\n')
    else:
        print("\n\n"+"------------------------------------")
        for i in down_list:
            if int(down_list[0][2])<int(i[0]):
                print(str(i[0])+"is picked")
        temp_list=[]
        for i in down_list:
            temp_list.append(i[0])
            temp_list.append(i[2])

        temp_list.sort()
        temp_list=set(temp_list)
        temp_list=list(temp_list)
        temp_list.sort()
        temp_list.reverse()
        print("\n\n"+"------------------------------------")
        print("Lift going down in order -->")
        print(*temp_list,sep='\n')

        print("\n\n"+"------------------------------------")
        for i in up_list:
            if int(up_list[0][2])>int(i[0]):
                print(str(i[0])+"is picked")
        temp_list=[]
        for i in up_list:
            temp_list.append(i[0])
            temp_list.append(i[2])
        temp_list.sort()
        
        temp_list=set(temp_list)
        temp_list=list(temp_list)
        temp_list.sort()
        print("\n\n"+"------------------------------------")
        print("Lift going up in order -->")
        print(*temp_list,sep='\n')


if __name__ == "__main__":
    obj=elevator()
