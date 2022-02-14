"""
Datos de entrada
Distancia recorrida en kilometros =k = int
Datos de salida
Pago que debe realizar el cliente = precio = int
"""
# Entradas
k=int(input( "Inserte la distancia recorrida por usten en kilometros : "))
# Caja Negra 
d=(k-1000) 
Precio=""
if (k<= 300):
    precio= 50000
elif(k>300 and k<1000):
    precio= (70000+(30000*(k-300)))
elif(k>1000):
    precio= ((150_000+(9000*(d)))+(((k-d)-300)*30000))
# Salidas 
print("tiene que pagar", precio)
