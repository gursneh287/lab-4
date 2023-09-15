N = int(input("enter N:"))
sum = 0
while N!=0:
    sum = sum+(N%10)
    N//10
print(sum)