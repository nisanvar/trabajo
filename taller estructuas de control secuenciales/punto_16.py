"""
datos de entrada
galones surtidos-->gs-->float
datos de salida
precio a cobrar-->pc
"""
#entrada
gs=float(input("digita gasolina surtida "))
#caja negra
l=(gs*3785)
pc=(l*50000)
#salida
print("lo que debe pagar es ",pc)