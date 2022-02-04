"""
datos de entrada
precio-->p-->int
datos de salida
precio final-->pf-->int
"""
#entrada
p=int(input("precio"))
#caja negra
pf=int(input(p-(p*0.15)))
#salida
print("el precio final es: ",pf)