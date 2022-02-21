
lista=[]
  
while True:
    n=float(input("ponga 1 para poner alturas  y  0 para sacar el mayor "))
    if(n==1):
        s=float(input())
        lista.append(s)
        continue
    elif(n==0):
        print("",max(lista))
        break
    