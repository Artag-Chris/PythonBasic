agenda=[]
#colocar ciudades y direcciones sin lista 
#como funciona la creacion y el update de un diccionario?
dirContacto={}
#data={0:{"idContacto" : "123" ,"nombre" : "emmanuel","email":"dfe", "movil" :"3434", "ubicacion":{},"ciudadNac":"Buc", "edad": "18"}}
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
        isAddItem=True
        while isAddItem==True:
            idContacto=input("Id del contacto : ")
            nombre=input("Nombre del contacto : ")
            email=input("E-mail del contacto : ")
            movil=input("Tel Movil del contacto : ")
            #no hace nada
            valor=len(dirContacto)
            contacto={
                "idContacto":idContacto,
                "nombre": nombre,
                "email": email,
                "movil": movil,
                "ubicacion":{}
            }
            dirContacto.update({idContacto:contacto})
            #agenda.append(contacto)
            rta=input("Desea ingresar otro contacto S o N")
            if rta.upper()=="S":
                isAddItem=True
            elif rta.upper()=="N":
                isAddItem=False
    elif op==2:
        #dirContacto.update(data)
        print(dirContacto)
        #palabra=input("ingrese el Id a buscar")
        #for contacto in agenda:
            #for Key, valor in agenda.items():
                #if palabra in valor:
                    #print("Ok")
    elif op==3:
        palabra=input("Ingrese Id a buscar : ")
        #los diccionarios se recorren por key" llave" y value"valor" en el nombre del directorio con el .items
        #ese valorc es una variable de contador para los value "valores podria tener cualquier nombre" va cambiando de valor 
        for key, valorc in dirContacto.items():
            #si la key "llave" es igual a palabra(input) hace lo siguiente
            if str(key) == palabra:
                #este valor toma un numero que es la longitud que tiene el value de "ubicacion" si esta vacio sera 0
                valor=len(valorc["ubicacion"])
                ciudad=input("Ingrese ciudad para registrar : ")
                direccion=input("Ingrese direccion para registrar : ")
                #aqui encuentra "ubicacion" dentro del diccionario y le hace un update le agrega la nueva data
                valorc["ubicacion"].update({valor :{"ciudad" : ciudad, "direccion" : direccion}})
    elif op==4:
        rta=input("Desea Salir del programa S o N ")
        if rta.upper()=="S":
            isMenuActive=False
        elif rta.upper()=="N":
            isMenuActive=True