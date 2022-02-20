"""
datos de entrada 
    nivel de emoglobina-->e-->float
    edad años-->ea-->int
    edad meses-->em-->int
    sexo del paciente-->s-->int
datos de salida
    anemia-->a-->str
"""
#entrada
e=float(input("diguite el nivel de emoglobina "))
ea=int(input("diguite el numero de años "))
em=int(input("diguite el numero de mese "))
s=int(input("sexo del paciente (1: masculino/0:femanino) "))
#caja negra
emt=(ea*12)+em
a=""
if emt<=1:
    if e<13:
        a="positivo"
    else:
        a="negativo"
elif 2<emt<=6:
    if e<10:
        a="positivo"
    else:
        a="negativo"
elif 6<emt<=12:
    if e<11:
        a="positivo"
    else:
        a="negativo"
elif 12<emt<=60:
    if e<11.5:
        a="positivo"
    else:
        a="negativo"
elif 60<emt<=120:
    if e<12.6:
        a="positivo"
    else:
        a="negativo"
elif 120<emt<=180:
    if e<13:
        a="positivo"
    else:
        a="negativo"
elif (s==0):
    if 180<emt:
        if e<12:
            a="positivo"
        else:
            a="negativo"
elif (s==1):
    if 180<emt:
        if e<14:
            a="positivo"
        else:
            a="negativo"
#salidas
print(a)