"""
datos de entrada
costo de produccion-->cp-->int
precio a el publico-->p--<int
datros de salida
descuento-->d-->float
"""
#entrada
cp=int(input("dijite el dato de costo "))
p=int(input("dijite el precio a el publico "))
#caja negra
q=(cp-p)
d=(q*100)/cp
#salida
print("el descuento estaria en ",d,"%")