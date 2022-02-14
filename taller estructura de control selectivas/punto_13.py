"""
datos de entrada
fecha de nacimiento
"""

#entrada
fecha_nacimiento=input("Digite en este formato 'dd/mm/yy : ")
day,month,year = fecha_nacimiento.split("/")
dia_nacimiento=int(day)
mes_nacimiento=int(month)
año_nacimiento =int(year)

# Caja Negra 

import datetime
x = datetime.datetime.now() # Hora de la maquina
mes_actual = int(x.strftime("%m"))
año_actual = int(x.strftime("%Y"))
dia_actual = int(x.strftime("%d"))
edad=(año_actual-año_nacimiento)

if(mes_actual>mes_nacimiento):
    print(edad)
else:
    print(edad-1)

#caja negra
signo=""
if(22>=dia_nacimiento and 22<=dia_nacimiento and 11<=mes_nacimiento and 12>=mes_nacimiento):
    signo="sagitario"
elif(22>=dia_nacimiento and 20<=dia_nacimiento and 12>=mes_nacimiento and 1<=mes_nacimiento):
    signo="capricornio"
elif(12>=dia_nacimiento and 19>=dia_nacimiento and 1>=mes_nacimiento and 2<=mes_nacimiento):
    signo="acuario"
elif(20>=dia_nacimiento and 20<=dia_nacimiento and 2>=mes_nacimiento and 3<=mes_nacimiento):
    signo="piscis"
elif(21>=dia_nacimiento and 20<=dia_nacimiento and 3>=mes_nacimiento and 4<=mes_nacimiento):
    signo="aries"
elif(21>=dia_nacimiento and 21<=dia_nacimiento and 4>=mes_nacimiento and 5<=mes_nacimiento):
    signo="tauro"
elif(22>=dia_nacimiento and 21<=dia_nacimiento and 5>=mes_nacimiento and 6<=mes_nacimiento):
    signo="geminis"
elif(22>=dia_nacimiento and 22<=dia_nacimiento and 6>=mes_nacimiento and 7<=mes_nacimiento):
    signo="cancer"
elif(23>=dia_nacimiento and 23<=dia_nacimiento and 7>=mes_nacimiento and 8<=mes_nacimiento):
    signo="leo"
elif(24>=dia_nacimiento and 22<=dia_nacimiento and 8>=mes_nacimiento and 9<=mes_nacimiento):
    signo="virgo"
elif(23>=dia_nacimiento and 22<=dia_nacimiento and 9>=mes_nacimiento and 10<=mes_nacimiento):
    signo="libra"
elif(23>=dia_nacimiento and 21<=dia_nacimiento and 10>=mes_nacimiento and 11<=mes_nacimiento):
    signo="escorpio"
#salida
print("el signo es",signo)
