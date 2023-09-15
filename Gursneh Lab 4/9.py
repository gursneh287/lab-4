sen = (input("enter a sentence:"))
i = 0
uc,lc,dg,sp = 0,0,0,0
while i<len(sen):
    if ord(sen[i]) >= 65 and ord(sen[i])<=90:
        uc += 1
    elif ord(sen[i]) >= 97 and ord(sen[i])<=122:
        lc+=1
    elif ord(sen[i]) >= 48 and ord(sen[i])<=57:
        dg+=1
    else:
        sp+=1
    i+=1
print("uc=",uc,"lc=",lc,"dg=",dg,"sp=",sp)