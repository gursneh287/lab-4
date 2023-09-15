a = int(input("enter coefficient of x**2:"))
b = int(input("enter coefficient of x:"))
c = int(input("enter constant:"))
D = (b**2)-(4*a*c)
x1 = (-b+(D**0.5))/2*a
x2 = (-b-(D**0.5))/2*a
if D > 0:
    print("x1=",round(x1,2),"x2=",round(x2,2))
elif D == 0:
    print("x=",round(x1,2))
elif D<0:
    print("roots are not real")
