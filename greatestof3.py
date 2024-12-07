a=int(input("enter any  A number"))
b=int(input("enter any  B number"))
c=int(input("enter any  C number"))

if(a>b and a>c):
    print("A is big")
else:
    if(b>c):
        print("B is big")
    else:
        print("C is big")