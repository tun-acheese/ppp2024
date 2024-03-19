x=int(input("x좌표를 입력하시오."))
y=int(input("y좌표를 입력하시오."))

if x>0 and y>0:
    print("1")
elif x>0 and y<0:
    print("4")
elif x<0 and y>0:
    print("2")
else:
    print("3")
