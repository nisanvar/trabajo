"""
Datos de entrada
valor de entrada 1 = v1 = int
valor de entrada 2 = v2 = int
Datos de salida
Caso afirmativo = " Los valores de p y q satisfacen la expresion "
Caso Negativo = " Los valores de p y q no satisfacen la expresion "
"""
# Entradas
v1=int(input( "Inserte el valor que le dara a P : "))
v2=int(input( "Inserte el valor que le dara a Q : "))
# Caja Negra 
respuesta=''
if ((v1**3 + v2**4 - 2*v1**2) > 680):
    respuesta=(f"v1 es : {v1} y Q :{v2} satisfacen la expresion ")
else:
    respuesta=(f"v1 es :{v1} y Q :{v2} no satisfacen la expresion ")
# Salidas 
print("",respuesta)
