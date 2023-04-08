import vv
import sys
file = open("input.txt","w")
file.truncate()
q=1
while True:
    a=input("Enter the source and destination:\n")
    file.write(a+"\n")
    q=input("Want to enter one more? 0 or 1  ")
    if int(q)==0:
        file.close()
        obj=vv.elevator()
        obj.ele()
        sys.exit()
