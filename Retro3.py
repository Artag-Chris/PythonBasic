import os
import time
#listas de la primera parte "registrar equipo y jugadores"
equipo=[]
equipoParticipante=[]
provicional=[]
#lista de fechas
fechas=[]
posicion=int(0)
#organizar front-end
#metodo para imprimir la tabla de posiciones
def valores(*args):
    for i in args:
        print(f" Equipo {i[1]} sus datos son {i[6]} ") 

isActivateMenu=True
isAddEquipo=True
isAddProveedor=True
isAddjugador=True
op=0
while isActivateMenu==True:
    #menu principal hay que modificarlo
    print("1.Ingresar Equipo o Jugador\n2.Ingresar Datos de cada partido\n3.Buscar jugador por Codigo del equipo\n4.Tabla de posiciones de mayor a menor\n5.Ver todas las fechas\n6.Salir")
    op=int(input())
    if op==1:
        os.system('cls')
        isAddEquipo=True
        equipoParticipante=[]
        while isAddEquipo==True:
            #submenu que agrege para facilitar el registro de equipos y jugadores por separado        
            opc=0
            print("Selecione una opcion \n1. registrar un equipo al torneo\n2. ingresar un jugador a la plantilla de jugadores\n3. Salir y ver equipos")
            opc=int(input())
            if opc==1:
                os.system('cls')
                isAddEquipo=True
                codigo=input("Ingrese el codigo del Equipo :")
                nombre=input("Ingrese el nombre del Equipo :")
                pais=input("Ingrese la confederacion a la que pertenece el Equipo :")
                #la penultima lista que se crea es donde vendra la informacion de la plantilla 
                #la ultima lista es donde se guardara la fecha y los puntos ganados
                #el diccionario es donde guardare datos de partidos y numeros
                equipoParticipante=[]
                #posicion esta en primer lugar para que el sort los organize en forma numerica
                equipoParticipante=[posicion,codigo.upper(),nombre.upper(),pais.upper(),[],[],{}]
                equipo.append(equipoParticipante)
                rta=input("Desea Ingresar un equipo al torneo S o N : ")
                if rta.upper()=="S":
                    os.system('cls')
                    isAddEquipo=True
                    codigo=input("Ingrese el codigo del Equipo : ")
                    nombre=input("Ingrese el nombre del Equipo : ")
                    pais=input("Ingrese la confederacion a la que pertenece el Equipo :")
                    equipoParticipante=[]
                    equipoParticipante=[posicion,codigo.upper(),nombre.upper(),pais.upper(),[],[],{}]
                    equipo.append(equipoParticipante)
                    print("solo se pueden ingresar equipos por tandas de 2 ")
                elif rta.upper()=="N":
                    isAddEquipo=False
                else:
                    print("Respuesta no valida")
                    isAddEquipo=True
                   
            elif opc==2:
                os.system('cls')
                palabra=input("Ingrese el codigo del equipo a Buscar : ")
                isAddJugador=True
                provicional=[]
                for item in equipo:
                    if palabra.upper() in item:
                        while isAddJugador==True:
                            nombre=input("Ingrese nombre del jugador : ")
                            posicion=input("Ingrese posicion del jugador : ")
                            provicional.extend([nombre,posicion])
                            #item[4] hace referencia al 5 puesto de la lista donde se encuentre el id del equipo
                            item[4].extend(provicional)
                            provicional=[]
                            print(item[4])
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
                os.system('cls')
                print(equipo)
                
            else:
                print("Respuesta no valida")
                isAddJugador=True
    elif op==2:
        os.system('cls')
        #menu donde registrare los puntos par cada equipo y las fechas quedaran registradas en su propia gran lista
        fecha=input("Ingrese la fecha en orden numerico : ")
        equipoA=""
        equipoA=input("Ingrese el id del equipo que juega como en casa : ")
        golesA=int(input("Ingrese la cantidad de goles que lograron : "))
        equipoB=""
        equipoB=input("Ingrese el id del equipo que juega como visitante : ")
        golesB=int(input("Ingrese la cantidad de goles que lograron : "))
        if golesA > golesB:
            print(f" el equipo ganador es equipo {equipoA} con {golesA} recibira +3 puntos  ")
            jornada=[]
            jornada=[fecha,equipoA.upper(),golesA,equipoB.upper(),golesB]
            fechas.append(jornada)
            for item in equipo:
                if equipoA.upper() in item:
                    #item[0] hace referencia a el primer item de la lista que es provicional
                    item[0]=+3
                    item[5].extend([3])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    #item[6] hace referencia al diccionario que use para imprimir mejor la info
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesA})
                   
                  
            #me invente este ciclo por separado para buscar la id del equipo perdedor y colocarle su +0
            for item in equipo:
                if equipoB.upper() in item:
                    item[5].extend([0])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesB})
                    print(equipo)
                    time.sleep(3)
                    os.system('cls')

        elif golesA < golesB:
            print(f" el equipo ganador es equipo {equipoB} con {golesB} recibira +3 puntos  ")
            jornada=[]
            jornada=[fecha,equipoA.upper(),golesA,equipoB.upper(),golesB]
            fechas.append(jornada)
            for item in equipo:
                if equipoB.upper() in item:
                    item[0]=int(+3)
                    item[5].extend([3])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesB})
                   

            for item in equipo:
                if equipoA.upper() in item:
                    item[5].extend([0])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesA})
                    print(equipo)
                
        elif golesA == golesB:
            print(f" los equipos empataron y ambos recibiran +1 punto ")
            jornada=[]
            jornada=[fecha,equipoA.upper(),golesA,equipoB.upper(),golesB]
            fechas.append(jornada)
            for item in equipo:
                if equipoB.upper() in item:
                    item[0]=int(+1)
                    item[5].extend([1])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesA})
                    
                
            for item in equipo:
                if equipoA.upper() in item:
                    item[0]=int(+1)
                    item[5].extend([1])
                    contadorPartidos = len(item[5])
                    contadorGanados = item[5].count(3)
                    contadorPerdidos = item[5].count(0)
                    contadorEmpatados = item[5].count(1)
                    item[6].update({"Partidos jugados": contadorPartidos, "partidos ganados": contadorGanados, "Partidos Perdidos":contadorPerdidos,"Partidos empatados":contadorEmpatados,"Total Goles":+golesA})
      
                    print(equipo)

        print(fechas)             
    elif op==3:
        os.system('cls')
        #aqui se buscaran los jugadores del equipo
        palabra=input("Ingrese el codigo del equipo a Buscar : ")
        for item in equipo:
            if palabra.upper() in item:
                print(f"lista de jugadores para {palabra.upper()} {item[4]} ")
                
    elif op==4:
        os.system('cls')
        #tabla de posiciones
        #sorted me ayuda a arreglar la lista por orden numerico y el reverse=True ayuda a que valla de mayor a menor
        equipoX = sorted(equipo,reverse=True)
        print(valores(*equipoX))     
    elif op==5:
        os.system('cls')
        #fechas para comprovar datos
        print(fechas)
    elif op==6:
        rta=input("Desea Abandonar el Programa S o N : ")
        if rta.upper()=="S":
            isActivateMenu=False
        elif rta.upper()=="N":
            isActivateMenu=True
        else:
            print("Respuesta no valida")
            isActivateMenu=True
   
        
            
