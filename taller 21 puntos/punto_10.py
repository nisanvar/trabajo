"""
datos de entrada
chelines austricos-->ca-->float
dracmas griebos-->dg-->float
pesetas-->pe-->int
daros de salida
pesetas-->q-->float
francos franceses-->w-->float
dolares-->e-->float
libras italianas-->r-->float
"""
#entrada
ca=float(input("ponga en chelines austricos "))
dg=float(input("ponga en dracmas griegos "))
p=float(input("ponga en pesetas "))
#caja negra
q=(ca*956.871)/100
w=((dg*88.607)/100)/20.110
e=p/122.499
r=(p*100)/9.289
#salida
print("cerían ",q,"pesetas")
print("ceían",w,"francos franceses")
print("cerían",e,"dolares")
print("cerían",r,"libras italianas")
