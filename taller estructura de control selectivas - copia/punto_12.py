"""
datos de entrada
cantidad en pesos colombianos-->dt-->folat
datos de salida

"""
#entrada
a=float(input("digite la cantidad en pesos colombianos: "))
#caja negra
lista=()
for i in (100000,50000,20000,10000,5000,2000,1000,500,200,100,50):
    if a >= i:
        lista.append(int(a/i)*i)
        a=a-int(a/i)*i
    else:
        a=a
lista0=str(lista)(1-1)
#saldia
print(lista0 ,"/n")


