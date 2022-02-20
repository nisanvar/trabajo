"""
datos de entrada
temperatura-->t-->float
datos de salida
deporte-->d-->str
"""
#entrada
t=float(input("digite la tempeteratura "))
#caja negra
deporte=""
if(t>85):
    deporte="natacion "
elif(t>70 and t<=85):
    deporte="tenis "
elif(t>32 and t<=70):
    deporte="golf"
elif(t>12 and t<=32):
    deporte="esqui "
elif(t<=100):
    deporte="marcha"
else:
    deporte="no se encuentra en el rango"
#salida
print("el peporte es ",deporte)
