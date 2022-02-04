"""
datos de entrada
sueldo-->s-->int
datos de salida
total-->t-->float
"""
#entrada
s=int(input("ponga su sueldo base "))
vent=int(input("ponga la ganancia total de la ventas "))
#caja negra
q=(vent*0.10)
w=q+s
#salida
print("gano por sus 3 ventas: ",q)
print("en total: ",w)
