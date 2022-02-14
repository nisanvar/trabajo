"""
datos de entrada
lectura anteriror-->la-->float
lecctura actual-->lc-->float
datos de salida

"""
#entrada


la=float(input("digite el consumo anterior: "))
lc=float(input("digite el consumo actual: "))
#caja negra
q=(la-lc)
costo=""
if(0<=q and q>=100):
    costo=(4600) 
elif(101<=q and q>=300):
    costo=(80000)
elif(301<=q and q>=500):
    costo=(100000)
elif(501<=q):
    costo=(120000)
w=q*costo
#salida
print(f"deve pagar",w)

