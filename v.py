# sumOfTwo(a,b,uv)=1||0
#2 solutions O=n2 and O=linear n  using composite set
class C1:
    def sumOfTwoOne(self,a,b,uv):
        # return (a,b,uv)
        for i in a:
            for j in b:
                if (int(i)+int(j))==int(uv):
                    return True
                else:
                    continue
        return False
        
    
    def sumOfTwoTwo(self,a,b,uv):
        c_set=[]
        for i in b:
            c_set.append(int(uv)-int(i))

        for i in a:
            if i in c_set:
                return (True,c_set)
            else:
                continue
        return False


if __name__ == "__main__":
    obj=C1()
    a=[1,2,3]
    b=[10,20,30,40]
    uv=42
    ans1=obj.sumOfTwoOne(a,b,uv)
    ans2=obj.sumOfTwoTwo(a,b,uv)
    print(ans1)
    print(ans2)
