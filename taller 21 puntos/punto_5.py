"""
datos de entrada
nota_1-->n1-->int
nota_2-->n2-->int
nota_3-->n3-->int
examen_final-->ef-->int
trabajo_final-->tf-->int
datos de salida
calificacion de la materia-->cf-->float} 
"""
#entrada
n1=int(input("ponga nota 1"))
n2=int(input("ponga nota 2"))
n3=int(input("ponga nota 3"))
ef=int(input("ponga nota del examen"))
tf=int(input("nota trabajo final"))
#caja negra
nf=((n1+n2+n3)/3)*0.55
q=ef*0.3
w=tf*0.15
cf=(nf+q+w)
#salida
print("la calificacion final es: ",cf)
