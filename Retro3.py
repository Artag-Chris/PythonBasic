equipo=[]
provicional=[]
#listas de la primera parte "registrar equipo y jugadores"
compras=[]
isActivateMenu=True
isAddEquipo=True
isAddProveedor=True
isAddjugador=True
op=0
while isActivateMenu==True:
    #menu principal hay que modificarlo
    print("1.Ingresar Equipo\n2.Ingresar Datos de cada partido\n3.Ver proveedor por Equipo\n4.Comprar\n5.Listar Equipos\n6.Calcular compra total\n7.Salir")
    op=int(input())
    if op==1:
        isAddEquipo=True
        while isAddEquipo==True:
            #submenu que agrege para facilitar el registro de equipos y jugadores
            #hay que arreglar o buscar solucion a la opcion que pasa de equipo a pais
            opc=0
            print("Selecione una opcion \n1. registrar un equipo al torneo\n2. ingresar un jugador a la plantilla de jugadores\n3. Salir")
            opc=int(input())
            if opc==1:
                codigo=input("Ingrese el codigo del Equipo :")
                nombre=input("Ingrese el nombre del Equipo :")
                pais=input("Ingrese el pais del Equipo :")
                plantel=int(input("Ingrese el  numero del plantel del Equipo : "))
                #la penultima lista que se crea es donde vendra la informacion de la plantilla 
                #la ultima lista es donde se guardara la fecha y los puntos ganados
                equipoParticipante=[codigo.upper(),nombre.upper(),pais.upper(),plantel,[],[]]
                equipo.append(equipoParticipante)
                rta=input("Desea Ingresar un jugador del equipo S o N : ")
                if rta.upper()=="S":
                    isAddJugador=True
                    nombre=input("Ingrese Nombre del jugador : ")
                    posicion=input("Ingrese posicion del jugador : ")
                    provicional.append([nombre,posicion])
                    provicional=[]
                    rta=input("Desea Ingresar otro jugador S o N : ")
                    if rta.upper()=="S":
                        isAddJugador=True
                    elif rta.upper()=="N":
                        isAddJugador=False
                    else:
                        print("Respuesta no valida")
                        isAddJugador=True
                elif rta.upper()=="N":
                    isAddJugador=False
                else:
                    print("Respuesta no valida")
                    isAddJugador=True
            elif opc==2:
                palabra=input("Ingrese el codigo del equipo a Buscar : ")
                isAddJugador=True
                provicional=[]
                for item in equipo:
                    if palabra.upper() in item:
                        while isAddJugador==True:
                            nombre=input("Ingrese nombre del jugador : ")
                            posicion=input("Ingrese posicion del jugador : ")
                            provicional.append([nombre,posicion])
                            rta=input("Desea Ingresar otro Jugador S o N : ")
                            if rta.upper()=="S":
                                isAddJugador=True
                            elif rta.upper()=="N":
                                isAddJugador=False
                            else:
                                print("Respuesta no valida")
                                isAddJugador=True
                item[4].extend(provicional)  
                provicional=[]    
            elif opc==3:
                isAddEquipo=False
                isAddJugador=False
                print(equipo)
            else:
                print("Respuesta no valida")
                isAddJugador=True
    elif op==2:
        palabra=input("Ingrese el codigo del equipo para registrar la fecha : ")
        isAddProveedor=True
        prov=[]
        for item in equipo:
            if palabra.upper() in item:
                while isAddProveedor==True:
                    idprov=input("Ingrese Identificacion Prov : ")
                    nombrep=input("Ingrese Nombre Prov : ")
                    ciudad=input("Ingrese ciudad Prov : ")
                    prov.append([idprov,nombrep,ciudad])
                    rta=input("Desea Ingresar otro proveedor S o N : ")
                    if rta.upper()=="S":
                        isAddProveedor=True
                    elif rta.upper()=="N":
                        isAddProveedor=False
                    else:
                        print("Respuesta no valida")
                        isAddProveedor=True
                item[5].extend(prov)
                    
    elif op==3:
        palabra=input("Ingrese el codigo del producto a Buscar : ")
        for producto in equipo:
            if palabra.upper() in producto:
                for prov in producto[4]:
                    print(f"Id Proveedor : {prov[0]} | Nombre Proveedor : {prov[1]}",end="\n")
                
    elif op==4:
        isBuying=True
        while isBuying==True: 
            palabra=input("Ingrese el codigo del producto a Comprar : ")
            cantidad=int(input("Ingrese Cantidad a Comprar : "))
            provid=input("Ingrese el codigo del Proveedor : ")
            valorc=float(input("Ingrese Cantidad a Comprar : "))
            isFound=False
            for producto in equipo:
                if palabra.upper() in producto:
                    for prov in producto[4]:
                        if provid in prov:
                            isFound=True
                    if isFound==True:
                        buy=([producto[0],producto[1],cantidad,valorc,provid])
                        if producto[3]!=valorc:
                            producto[3]=valorc
                        compras.append(buy)
                    else:
                        print("No se puede comprar")
            rta=input("Desea registrar otra compra S o N")
            if rta.upper()=="S":
                isBuying=True
            else:
                isBuying=False          
    elif op==5:
        for item in equipo:
            print(f"Codigo : {item[0]} Nombre Producto: {item[1]} Cantidad Disponible : {item[2]} Valor Unitario : {item[3]}",end="\n")
    elif op==6:
        totalcompra=0
        header=["Codigo","Nombre del producto","Cantidad","Valor Unit","Subtotal"]
        print(f"{header[0]} {header[1]} {header[2]} {header[3]} {header[4]}")
        for buy in compras:
            print(f"{buy[0].ljust(6)} {buy[1].ljust(19)} {str(buy[2]).ljust(8)} {str(buy[3]).ljust(10)} {(buy[2]*buy[3])}",end="\n")
            totalcompra=totalcompra+(buy[2]*buy[3])
        print(f"Total de la Compra : {totalcompra}")      
    elif op==7:
        rta=input("Desea Abandonar el Programa S o N : ")
        if rta.upper()=="S":
            isActivateMenu=False
        elif rta.upper()=="N":
            isActivateMenu=True
        else:
            print("Respuesta no valida")
            isActivateMenu=True
            
