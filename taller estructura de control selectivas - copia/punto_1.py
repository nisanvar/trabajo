"""
datos de entrada
invercion-->i-->int
interes-->t-->float
datos de salida
dinero-->dinero-->float
"""
#entrada
i=int(input("digite su invercion "))
t=float(input("digite el interes "))
#caja negra
q=(t*i)/100
dinero=""
if(i>100000):
    dinero=(" se re invierte y tendria ",(i+q))
else:
    dinero="no se re invierte "
#saida
print(dinero)