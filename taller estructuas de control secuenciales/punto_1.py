"""
datos de entrada
edad_uno-->e_uno-->int
edad_dos-->e_dos-->int
edad__tres-->e_tres-->int
datos de salida 
promedio-->p-->float
"""
#entrada
e_uno=int(input("digite edad uno: "))
e_dos=int(input("digite edad dos: "))
e_tres=int(input("digite edad tres: "))
#caja negra
p=(e_uno+e_dos+e_tres)/3
#salida
print("el promedio de edad es: ",p)
