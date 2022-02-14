"""
datos de entrada
salario neto-->sn-->float
ventas totales-->vt-->int
ventas del vendedor 1-->v1-->int
ventas del vendedor 2-->v2-->int
ventas del vendedor 3-->v3-->int
datos de salida
sueldo final-->sf-->float
"""
#entrada
sn=float(input("digite el salario neto "))
vt=int(input("dijite las ventas totales "))
v1=int(input("dijite las ventas del vendedor 1 "))
v2=int(input("dijite las ventas del vendedor 2 "))
v3=int(input("dijite las ventas del vendedor 3 "))
#caja negra
q=(vt*0.33)
w=(sn*0.2)
salario=""
if(v1>q):
    salario="su sueldo es ",(sn+w)
else:
    salario="su sueldo es",sn
if(v2>q):
    salario="su sueldo es ",(sn+w)
else:
    salario="su sueldo es",sn
if(v3>q):
    salario="su sueldo es ",(sn+w)
else:
    salario="su sueldo es",sn
#salida
print(salario)

