"""
datos de entrada 
tarea de matematicas 1-->tm1-->float
tarea de matematicas 2-->tm2-->float
tarea de matematicas 3-->tm3-->float
examen de matematicas-->em-->float
tarea de fisica 1-->tf1-->float
tarea de fisica 2-->tf2-->float
examen de fisica-->ef-->float
tarea de quimcia 1-->tq1-->float
tarea de quimcia 2-->tq2-->float
tarea de quimcia 3-->tq3-->float
examen de quimica-->eq-->float
"""
#entrada
tm1=float(input("ponga la nota en la tarea 1 de matematicas"))
tm2=float(input("ponga la nota en la tarea 2 de matematica"))
tm3=float(input("ponga la nota en la tarea 3 de matematica"))
em=float(input("ponga la nota del examen de matematicas"))
tf1=float(input("ponga la nota de la tarea 1 de fisica"))
tf2=float(input("ponga la nota de la tarea 2 de fisica"))
ef=float(input("ponga la nota del examen de fisica"))
tq1=float(input("ponga la nota de la tarea 1 de quimica "))
tq2=float(input("ponga la nota de la tarea 2 de quimica "))
tq3=float(input("ponga la nota de la tarea 3 de quimica "))
eq=float(input("ponga la nota del examen de quimica"))
#caga negra
pmt=(((tm1+tm2+tm3)/3)*0.1)
pem=(em*0.9)
pfm=(pmt+pem)
pf=(((tf1+tf2)/2)*0.2)
pef=(ef*0.8)
pff=(pf+pef)
pq=(((tq1+tq2+tq3)/3)*0.15)
peq=(eq*0.85)
pfq=(pq+peq)
pn=(pfm+pff+pfq)/3
#salida
print("su promedio en matematicas es ",pfm)
print("su promedio en fisicsa es ",pff)
print("su promedio en quimica es ",pfq)
print("el promedio de las 3 es ",pn)


