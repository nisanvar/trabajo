"""
datos de entrada
mujeres-->m-->int
hombres-->h-->int
datos de salida
"""
#entrada
m=int(input("escriba numero de hombres: "))
h=int(input("escriba numero de mujeres: "))
#caja negra
t=m+h
q=(m*100)/t
w=(h*100)/t
#salida
print("el promedio de hombres es: ",w,"%")
print("el promedio de mujeres es: ",q,"%")