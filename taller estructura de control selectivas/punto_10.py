"""
datos de entrada
cat-->categoria-->int
sueldo bruto-->sb-->int
datos de salida
"""
#entrada
cat=int(input("ponga la categoria "))
sb=int(input("digite su sueldo neto "))
#caja negra
aumento=""
if(cat==1 and sb==5000000):
    aumento=(sb*0.10)
elif(cat==2 and sb==4300000):
    aumento=(sb*0.15)
elif(cat==3 and sb==3600000):
    aumento=(sb*0.20)
elif(cat==4 and sb==2000000):
    aumento=(sb*0.40)
elif(cat==5 and sb==900000):
    aumento=(sb*0.6)
else:
    aumento="no hay aumento"
ns=""
if(cat==1 and sb==5000000):
    ns=((sb*0.10)+sb)
elif(cat==2 and sb==4300000):
    ns=((sb*0.15)+sb)
elif(cat==3 and sb==3600000):
    ns=((sb*0.20)+sb)
elif(cat==4 and sb==2000000):
    ns=((sb*0.40)+sb)
elif(cat==5 and sb==900000):
    ns=((sb*0.6))+sb
else:
    ns=sb
#salida
print("la categoria es: ",cat, "el aumento es de: ", aumento,"y el sueldo final es: ",ns)
