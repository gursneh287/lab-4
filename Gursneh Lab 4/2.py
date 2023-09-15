x = int(input("enter X:")) 
Y = int(input("enter Y:")) 
N = int(input("enter N:")) 
i = x+1
while i<=Y:
    if i%N == 0:
        print(i)
    i += 1
