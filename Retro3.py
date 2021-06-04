#listas de la primera parte "registrar equipo y jugadores"
equipo=[]
equipoParticipante=[]
provicional=[]
#lista de fechas
fechas=[]
#se debe crear una forma que asi gane 0 puntos en una fecha el equipo perdedor gane un [0]
#organizar front-end
compras=[]
isActivateMenu=True
isAddEquipo=True
isAddProveedor=True
isAddjugador=True
op=0
while isActivateMenu==True:
    #menu principal hay que modificarlo
    print("1.Ingresar Equipo o Jugador\n2.Ingresar Datos de cada partido\n3.Buscar jugador por Codigo del equipo\n4.Tabla de posiciones\n5.Listar Equipos")
    op=int(input())
    if op==1:
        isAddEquipo=True
        equipoParticipante=[]
        while isAddEquipo==True:
            #submenu que agrege para facilitar el registro de equipos y jugadores         
            opc=0
            print("Selecione una opcion \n1. registrar un equipo al torneo\n2. ingresar un jugador a la plantilla de jugadores\n3. Salir")
            opc=int(input())
            if opc==1:
                codigo=input("Ingrese el codigo del Equipo :")
                nombre=input("Ingrese el nombre del Equipo :")
                pais=input("Ingrese la confederacion a la que pertenece el Equipo :")
                plantel=int(input("Ingrese el  numero del plantel del Equipo : "))
                #la penultima lista que se crea es donde vendra la informacion de la plantilla 
                #la ultima lista es donde se guardara la fecha y los puntos ganados
                equipoParticipante=[]
                equipoParticipante=[codigo.upper(),nombre.upper(),pais.upper(),plantel,[],[]]
                equipo.append(equipoParticipante)
                #cambiar este menu por ingresar otro equipo
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
                            provicional.extend([nombre,posicion])
                            item[4].extend(provicional)
                            provicional=[]
                            print(equipoParticipante)
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
        fecha=input("Ingrese la fecha en orden numerico : ")
        equipoA=input("Ingrese el id del equipo que juega como en casa : ")
        golesA=input("Ingrese la cantidad de goles que lograron : ")
        equipoB=input("Ingrese el id del equipo que juega como visitante : ")
        golesB=input("Ingrese la cantidad de goles que lograron : ")
        if golesA > golesB:
            print(f" el equipo ganador es equipo {equipoA} con {golesA} recibira +3 puntos  ")
            jornada=[fecha,equipoA.upper(),golesA,equipoB.upper(),golesB]
            fechas.append(jornada)
            for item in equipo:
                if equipoA.upper() in item:
                    item[5].extend([3])
                    print(equipo)
        elif golesA < golesB:
            print(f" el equipo ganador es equipo {equipoB} con {golesB} recibira +3 puntos  ")
            Fechas=[fecha,equipoA,golesA,equipoB,golesB]
            for item in equipo:
                if equipoB.upper() in item:
                    item[5].extend([3])
                    print(equipo)
        elif golesA == golesB:
            print(f" los equipos empataron y ambos recibiran +1 puntos ")
            Fechas=[fecha,equipoA,golesA,equipoB,golesB] 
            for item in equipo:
                if equipoB.upper() and equipoA in item:
                    item[5].extend([1])
                    print(equipo)
        #fechas=[fecha,equipoA,golesA,equipoB,golesB]
        
        print(fechas)

        
                    
    elif op==3:
        palabra=input("Ingrese el codigo del equipo a Buscar : ")
        for item in equipo:
            if palabra.upper() in item:
                print(f"lista de jugadores para {palabra.upper()} {item[4]  } ")
                
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
            
