"""
datos de entrada
capital-->c-->int
datos de salida
g-->ganancia-->float
"""
#entrada
c=float(input("ingrese su capital"))
#caja negra
g=(c*0.2)/100
#salida
print("ganacia: ",g)
print("en total: ",(g+c))