"""
datos de entrada
presupuesto anual-->pa-->int
datos de salida
ginecologia-->g-->float
traumatoligia-->t-->float
pediatria-->p-->float
"""
#entrada
pa=int(input("digite el presupuesto anual"))
#caja negra
g=(pa*0.4)
t=(pa*0.3)
p=(pa*0.3)
#salida
print("el porcentaje para ginecologia es ",g,"&")
print("el porcentaje para traumatologia es ",t,"&")
print("el porcentaje para pediatria es ",p,"&")