n = int(input("enter number of terms:"))
n1 = 1
n2 = 1
count = 0
if n == 1:
    print("fibonacci sequence")
    print(n1)
elif n>1:
    print("fibonacci sequence")
    while count<n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1