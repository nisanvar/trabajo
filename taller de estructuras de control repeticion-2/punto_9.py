
a=0
d=0
g=0
while True:
    numero=int(input())
    if(numero==1):
        a=a+1
    elif(numero==2):
        g=g+1
    elif(numero==3):
        d=d+1
    elif(numero==4):
        break
print("MUITO OBRIGADO\nALcool:",a,"\n Gasolina:",g,"\n diesel:",d)
