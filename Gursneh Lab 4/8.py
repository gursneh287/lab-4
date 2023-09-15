n = int(input("enter a number:"))
i = 2
flag = 0
while i < n:
    if n%i == 0:
        flag = 1
    i += 1
if n==1:
    print("not aprime number")
elif flag == 1:
    print("not a prime number")
else:
    print("prime number")