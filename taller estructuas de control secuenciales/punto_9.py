"""
datos de entrada
precio de la hora-->ph-->int
horas trabajadas-->ht-->int
"""
#entrada
ph=int(input("ponga el precio de la hora "))
ht=int(input("ponga las horas trabajadas "))
#caja negra
p=ph*ht
w=0.2*p
sn=p-w
#salida
print("el suendo neto es: ",sn)