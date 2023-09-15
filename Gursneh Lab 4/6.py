N = str(input("enter integer:"))
a = len(N) - 1
n = 0
flag = 0
while n<=(a/2):
    if N[n]==N[a-n]:
       flag = 1
    else:
        flag = 2
    n += 1
if flag == 1:
    print("palindrome")
elif flag == 2:
    print("not a palindrome")