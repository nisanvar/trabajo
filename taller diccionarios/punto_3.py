usuarios = {
"iperurena": {
"nombre": "Iñaki",
"apellido": "Perurena",
"password": "123123"
},
"fmuguruza": {
"nombre": "Fermín",
"apellido": "Muguruza",
"password": "654321"
},
"aolaizola": {
"nombre": "Aimar",
"apellido": "Olaizola",
"password": "123456"
}
}
contador=0
while True:
    if(contador<=3):
        n=str(input("dgite el nombre: "))
        c=int(input("digite la contraseña: "))
        if (n=="Iñaki" and c==123123):
            print("Iñaki Perurena")
            break
        if (n=="Fermín" and c==654321):
            print("Fermín Muguruza")
            break
        if (n=="Aimar" and c==123456):
            print("Aimar Olaizola")
            break
        else:
            contador+=1
            continue
    else:
        print("cuenta bloqueada")
        break    