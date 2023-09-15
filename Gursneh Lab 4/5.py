N = int(input("enter N:"))
i = 1
fact = 1
if N>0:
    while i <= N:
        fact = fact*i
        i += 1
print(fact)