"""
Datos de entrada
Monto de la compra = monto_compra = int
Datos de salida
nombre del cliente = nombre_cliente
monto de la compra = monto_compra
monto a pagar = monto_pagar
descuento recibido = descuento
"""
# Entradas
cliente_nombre=str(input("Inserte el nombre del cliente"))
monto_compra=int(input( "Inserte el valor de la compra : "))
# Caja Negra 
monto_pagar=''
if(monto_compra<50_000):
    monto_pagar=(monto_compra)
elif(monto_compra>=50_000 and monto_compra<= 100_000):
    monto_pagar= (monto_compra-(monto_compra*0.05)) # descuento del 5% 
elif(monto_compra>100_000 and monto_compra <= 700_000):
    monto_pagar=(monto_compra-(monto_compra*0.11))
elif(monto_compra>700_000 and monto_compra<= 1_500_000):
    monto_pagar=(monto_compra-(monto_compra*0.18))
elif(monto_compra>1_500_000):
    monto_pagar=(monto_compra-(monto_compra*0.25))

descuento=''
if(monto_compra<50_000):
    descuento=("No hay descuento")
elif(monto_compra>=50_000 and monto_compra<= 100_000):
    descuento=(monto_compra*0.05) # descuento del 5% 
elif(monto_compra>100_000 and monto_compra <= 700_000):
    descuento=(monto_compra*0.11)
elif(monto_compra>700_000 and monto_compra<= 1_500_000):
    descuento=(monto_compra*0.18)
elif(monto_compra>1_500_000):
    descuento=(monto_compra*0.25)

# Salidas 
print(f"{cliente_nombre}")
print(f"El monto de la compra  es de : {monto_compra}")
print(f"El monto final a pagar es de : {monto_pagar}")
print(f"El descuento fue de: {descuento}")