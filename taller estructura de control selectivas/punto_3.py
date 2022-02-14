"""
datos de entrada
a-->float
b-->float
c-->float
d-->float
datos de salida
resultado-->resultado
"""
#entrada
a=int(input("digite el numero "))
b=int(input("digite el numero "))
c=int(input("digite el numero "))
d=int(input("digite el numero "))
#caja negra
resultado=""
if(0==d):
    resultado="la respuesta es ",(a-c)**2
if(d>0):
    resultado="la espuesta es", (a-b)**3

#salida
print("el resultado es",resultado)
