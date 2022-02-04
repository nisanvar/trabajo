"""
datos de entrada 
lado1-->a-->int
lado2-->b-->int
lado3-->c-->int

"""
#entrada
a=int(input("punga el lado 1"))
b=int(input("punga el lado 2"))
c=int(input("punga el lado 3"))
#caja negra
s=(a+b+c)/2
are=(s*(s-a)*(s-b)*(s-c))**(1/2)
#salida
print("el area es",are)
