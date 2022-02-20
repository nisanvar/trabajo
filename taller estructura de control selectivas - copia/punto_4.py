"""
datos de entrada
momto toal-->mt-->float
datos de salida

"""
#entradas
mt=float(input("digite el monto total"))
#caja negra

q=(mt*0.55)
w=(mt*0.3)
e=(mt*0.7)
r=(mt*0.2)
t=(mt*0.15)

if(mt>50000000):
    print("de su propio dinero aporta ",q)
    print("el prestamo a el banco es ",w)
    print("los intereses son de",(t*0.2))
else:
    print("de su propio dinero aporta " ,e)
    print("credito a al fabricande de",w)
    print("los intereses son de ",(w*0.2))