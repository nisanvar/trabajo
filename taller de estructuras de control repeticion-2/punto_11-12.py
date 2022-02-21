s=int(input("Consume licor (si o no) 1 es si 2 es no: "))
listas=[]
listas.append(s)
a=0
r=0
c=0
t=0
w=0
o=0
ar=0
listaar=[]
listasss=[]
listadad=[]
listamen=[]
listacer=[]
listawhi=[]
listaput=[]
while True:
    if((s==2)):
        print(f"Aguardiente {a} \nRon {r} \nCerveza {c} \nTequila {t} \nWhisky {w} \nOtro {o}")
        print(len(listas))
        print(len(listasss))
        print(sum(listamen))
        print(sum(listaput)/sum(listacer))
        print(len(listawhi)/len(listas))
        break
    elif(s==1):
        edad=int(input("¿Cual es tu edad? "))
        listadad.append(edad)
        sexo=str(input("¿Cual es tu sexo? 1 para masculino y 2 para femenino: "))
        ar=int(input("1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
        listas.append(ar)
        print("Nueva Encuesta")
        s=int(input("Desea continuar con la investigacion, si es 1, no es 2: "))
        if(ar==1):
            a=a+1
        elif(ar==2):
            r=r+1
        elif(ar==3):
            c=c+1
            listacer.append(c)
            if(ar==3 and edad>0):
                put=edad
                listaput.append(put)
                continue
        elif(ar==4):
            t=t+1   
        elif(ar==5):
            w=w+1
            listawhi.append(w)
        elif(ar==6):
            o=o+1   
        elif(edad>=0):
            listadad.append(edad)
            continue
        elif(edad<=18)and(sexo==2):
            yas=edad+sexo
            listasss.append(yas)
            continue
        elif(20>=edad<=25)and(sexo==1) and (ar!=5):
            men=edad+sexo
            if(ar!=5):
                listamen.append(men)
            continue