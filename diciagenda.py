agenda=[]
dirContacto={}
isMenuActive=True
isAddItem=True
op=0
print("********************************************")
print("***                                      ***")
print("**   Bienvenidos al Gestor de contactos   **")
print("***                                      ***")
print("********************************************")
input("*****  Press Enter to Continue  ************")
while isMenuActive==True:
    print("1. Agregar contacto\n2. Ver contacto\n3. Agregar Direccion a un contacto\n4. Salir")
    op=(int(input()))
    print(op)
    if op==1:
        while isAddItem==True:
            idContacto=input("Id del contacto : ")
            nombre=input("Nombre del contacto : ")
            email=input("E-mail del contacto : ")
            movil=input("Tel Movil del contacto : ")
            contacto={
                "idContacto":idContacto,
                "nombre": nombre,
                "email": email,
                "movil": movil,
                "ubicacion":{}
            }
            agenda.append(contacto)
            rta=input("Desea ingresar otro contacto S o N")
            if rta.upper()=="S":
                isAddItem=True
            elif rta.upper()=="N":
                isAddItem=False
    elif op==2:
        print(agenda)
        #palabra=input("ingrese el Id a buscar")
        #for contacto in agenda:
            #for Key, valor in agenda.items():
                #if palabra in valor:
                    #print("Ok")
    elif op==3:
        palabra=input("ingrese el Id a buscar : ")
        for contacto in agenda:
            for key, valor in contacto.items():
                if palabra in valor:
                    #estudiar losiguiente
                    valor=len(contacto["ubicacion"])
                    ciudad=input("Ingrese la ciudad : ")
                    direccion=input("Ingrese la Direccion : ")
                    contacto["ubicacion"].update({valor:{"ciudad":ciudad, "direccion": direccion }})
    elif op==4:
        rta=input("Desea Salir del programa S o N ")
        if rta.upper()=="S":
            isMenuActive=False
        elif rta.upper()=="N":
            isMenuActive=True