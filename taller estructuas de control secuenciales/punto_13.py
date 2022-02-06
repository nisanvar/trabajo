"""
datos de entrada
billetes de 50000-->n1-->int
blilletes de 20000-->n2-->int
blilletes de 10000-->n3-->int
blilletes de 5000-->n4-->int
blilletes de 2000-->n5-->int
blilletes de 1000-->n6-->int
blilletes de 500-->n7-->int
blilletes de 100-->n8-->int
"""
#entrada
n1=int(input("billetes de 50000 "))
n2=int(input("blilletes de 20000 "))
n3=int(input("blilletes de 10000 "))
n4=int(input("blilletes de 5000 "))
n5=int(input("blilletes de 2000 "))
n6=int(input("blilletes de 1000 "))
n7=int(input("blilletes de 500 "))
n8=int(input("blilletes de 100 "))
#caja negra
c=(n1*50000)+ (n2*20000)+(n3*10000)+(n4*5000)+(n5*2000)+(n6*1000)+(n7*500)+(n8*100)
#salida
print("tiene ",c)