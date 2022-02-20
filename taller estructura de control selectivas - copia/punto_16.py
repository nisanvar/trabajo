"""
Datos de entrada
valor de A --> A --> int
valor de B --> B --> int
valor de C --> C --> int
Datos de salida
valor de x--> x --> str
valor de x2--> x2 -->str
"""
#entradas
a=int(input("valor de a"))
s=int(input("valor de b"))
c=int(input("valor de c"))


#caja negra
e= s**2-4*a*c
if(e==0):
    x=x2=-s/(2*a)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
elif(e>0):
    x=(-s+(s**2-4*a*c))/(2*a)
    x2=(-s-(s**2-4*a*c))/(2*a)
    print("el valor de x1 es:", str(x), "y el valor de x2 es:", str(x2))
else:
    print("no tiene solucion en los reales")
#salida