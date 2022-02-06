"""
datos de entrada
numero de horas normales de trabajo-->ht-->float
pago por hora-->ph-->float
numero de horas extra-->hx-->float
actualizacion academica-->ac-->int
cantidad de hijos-->ch-->int
datos de salida

"""
#entradas
nh=float(input("ponga las horas trabajadas "))
ph=float(input("ponga el pago por hora "))
he=float(input("numero de horas extras trabajadas "))
ac=int(input("actualizacion academica "))
ch=int(input("cantidad de hijos "))
#caja negra
nt=nh*ph
t=((ph*0.25)*he)
st=nt+t
r=st*0.14
sa=((250000*ac)+(173000*ch)+(180000))
xt=sa+st-r
#salidas
print("el sueldo ganado es ",nt)
print("las deducciones son de ",r)
print("el resuldato por asicnaciones es de ",sa)
print("para un sueldo neto de ",xt)
