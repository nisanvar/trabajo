"""
datos de entrada
lectura anterior-->l1-->float
lectura actual-->l2-->float
costo del kilovatio-->ck-->float
datos de saldia
pago total-->pt-->float
"""
#entrada
l1=float(input("dijite la lectura anterior"))
l2=float(input("dijite la lectura actual"))
ck=float(input("ponga el costo del kilovatio"))
#caja negra
pt=(l1+l2)*ck
#salida
print("lo que paga es ",pt)