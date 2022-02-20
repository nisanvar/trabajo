"""
s>=1000
+=(((k**2)+1)/k)
k range 1,inf

"""
k=1
f=0
lista=[]
while (f<1000):
    f=(k**2+1)/k
    lista.append(f)
    k=k+1
    print(len(lista))
