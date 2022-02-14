"""
datos de entrada
salario bruto-->sb-->int
datos de salida
sueldo final-->sf-->int
"""
#entrada
sb=int(input("digite su sueldo "))
#caja negra
a=sb*0.15
s=sb*0.12
sueldo=""
if(sb<900000):
    sueldo="sueldo final es" ,(sb+a)
else:
    sueldo="su sueldo final es ",(sb+s)
#salida
print(sueldo)