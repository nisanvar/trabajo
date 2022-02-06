"""
datos de entrada
precio total-->pt-->float
precio de cuotas-->pc-->float
datos de saldida
extra-->x-->float
"""
#entrada
pt=float(input("precio total "))
pc=float(input("precio cuotas"))
#caje negra
x=pc-(pt/12)
#salida
print("el porcentaje extra es ",x,"%")