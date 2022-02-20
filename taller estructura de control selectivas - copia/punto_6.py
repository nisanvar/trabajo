"""
datos de entrada

datos de salida
"""
#entrada
a=int(input("digite en muero a "))
b=int(input("digite en muero b "))
c=int(input("digite en muero c "))
d=int(input("digite en muero d "))
#caja negra
q=a,b+1
w=a,b
d=a+1
n=int(str(a)+str(b)+str(c)+str(d))
#salida
print("el numero entero a redondair es: ", n)
if b<5 and c>=5:
    print("el numero entero a redondiar es: " ,q ,"00")
elif b<5 and c<5:
            print("el numero redondiado es: ",w ,"00")
else:
        print("el numero redondiado es :", d,"000")
           