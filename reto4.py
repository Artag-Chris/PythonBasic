import os
import time
from operator import *
#mejorar front-end
#adecuar opciones del menu colocar print de jugadores y de distintas fechas y ordenes de equipo 
#usar metodo de ljust o rjust 
#
equipo={}
fecha={}
isMenuActive=True
isAddEquipo=True
isSortActive=True
partidosJugados=int(0)
puntosGanados=int(0)
partidosGanados=int(0)
partidosEmpatados=int(0)
partidosPerdidos=int(0)
golesAFavor=int(0)
golesEnContra=int(0)
op=0
ops=0
print("********************************************")
print("***                                      ***")
print("**  Copa America 2021 Gestor de equipos   **")
print("***                                      ***")
print("********************************************")
input("*****  Press Enter to Continue  ************")
while isMenuActive==True:
    os.system('cls')
    print("1. Agregar equipo\n2. Ver equipo\n3. Agregar jugador\n4  Ver jugadores por equipo\n5  Ingresar Fecha\n6. Tablas de Posiciones\n7. Ver Fechas\n8. Salir")
    op=(int(input()))
    if op==1:
        os.system('cls')
        isAddEquipo=True
        while isAddEquipo==True:
            print("El id del equipo consta en las tres primeras letras del nombre del equipo ")
            idEquipo=input("Id del equipo : ")
            nombre=input("Nombre del equipo : ")            
            value={
                "nombre": nombre.upper(),
                "partidos Jugados": int(partidosJugados),
                "puntos Ganados":int(puntosGanados),
                "partidos Ganados": int(partidosGanados),
                "partidos Empatados": int(partidosEmpatados),
                "partidos Perdidos": int(partidosPerdidos),
                "goles A Favor": int(golesAFavor),
                "goles En Contra": int(golesEnContra),
                "jugadores":{}
            }
            equipo.update({idEquipo.upper():value})
            print(equipo[idEquipo.upper()]["nombre"])
            rta=input("Desea ingresar otro equipo S o N  ")
            if rta.upper()=="S":
                isAddEquipo=True
            elif rta.upper()=="N":
                isAddEquipo=False
    elif op==2:
        #ver equipos
        os.system('cls')
        print("Nombre         partidos Jugados ")
        for key,value in equipo.items():
            print(str(equipo[key.upper()]["nombre"]).ljust(9),str(equipo[key.upper()]["partidos Jugados"]).rjust(15))
        input("*****  Press Enter to Continue  ************")           
    elif op==3:   
        #ingresar jugador
        os.system('cls')
        palabra=input("Ingrese Id del equipo para ingresar nuevo jugador : ")
       
        for key, valorc in equipo.items():
            #si la key "llave" es igual a palabra(input) hace lo siguiente
            if str(key) == palabra.upper():
                #este valor toma un numero que es la longitud que tiene el value de "ubicacion" si esta vacio sera 0
                valor=len(valorc["jugadores"])
                nombreJugador=input("Ingrese nombre del Jugador para registrar : ")
                posicion=input("Ingrese posicion para registrar : ")
                #aqui encuentra "jugadores" dentro del diccionario y le hace un update le agrega la nueva data
                valorc["jugadores"].update({valor:{"nombre del jugador" : nombreJugador, "posicion del jugador" : posicion}})
                input("*****  Press Enter to Continue  ************")
    elif op==4:
        #ver jugadores en un equipo
        os.system('cls')
        palabra=input("Ingrese Id del equipo para ver sus jugadores : ")
        for key, valorc in equipo.items():
            if str(key) == palabra.upper():
                print(equipo[key]["nombre"])
                print("Nombre del jugador     posicion en el equipo")
                for i,j in equipo[key]["jugadores"].items():
                    print((str(equipo[key]["jugadores"][i]["nombre del jugador"])).ljust(10),str(equipo[key]["jugadores"][i]["posicion del jugador"]).rjust(25))
                    
                    
                input("*****  Press Enter to Continue  ************")

    elif op==5:
        os.system('cls')
        PartidoJugado=len(fecha)+1
        equipoA=input("ingrese el codigo del equipo que juega en casa ")
        golesA=int(input("ingrese la cantidad de goles alcanzados "))
        equipoB=input("ingrese el codigo del equipo visitante ")
        golesB=int(input("ingrese la cantidad de goles alcanzados "))
        datosFecha={
            "Equipo en casa" : equipoA.upper(),
            "Goles" :golesA,
            "Equipo visitante" : equipoB.upper(),
            "Goles visitante" : golesB
        }
        fecha.update({PartidoJugado:datosFecha})
        if golesA > golesB:
            print(f" el equipo ganador es equipo {equipoA} con {golesA} recibira +3 puntos  ")
            for key,value in equipo.items():
                if str(key) == equipoA.upper():
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    puntos=equipo[key].get("puntos Ganados")
                    puntos=(puntos+3)
                    ganados=equipo[key].get("partidos Ganados")
                    ganados=(ganados+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesA)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesB)
                    k={
                        "partidos Jugados":jugados,
                        "puntos Ganados":puntos,
                        "partidos Ganados":ganados,  
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(k)
                    
                    break




            for key,value in equipo.items():
                if str(key) == equipoB.upper():
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    perdidos=equipo[key].get("partidos Perdidos")
                    perdidos=(perdidos+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesB)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesA)
                    q={
                        "partidos Jugados":jugados,
                        "partidos Perdidos":perdidos,
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(q)
                    break
            print(f"ok equipo {str(key)} {value} ")       
                        
        elif golesA < golesB:
            print(f" el equipo ganador es equipo {equipoB} con {golesB} recibira +3 puntos  ")
            for key,value in equipo.items():
                if str(key) == equipoB.upper():                   
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    puntos=equipo[key].get("puntos Ganados")
                    puntos=(puntos+3)
                    ganados=equipo[key].get("partidos Ganados")
                    ganados=(ganados+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesB)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesA)
                    k={
                        "partidos Jugados":jugados,
                        "puntos Ganados":puntos,
                        "partidos Ganados":ganados,  
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(k)
                    break



            
                    print(f"ok equipo {str(key)} {value} ") 

            for key,value in equipo.items():
                if str(key) == equipoA.upper():
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    perdidos=equipo[key].get("partidos Perdidos")
                    perdidos=(perdidos+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesA)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesB)
                    q={
                        "partidos Jugados":jugados,
                        "partidos Perdidos":perdidos,
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(q)
                    break     

        elif golesA == golesB:
            print(f" fue un empate ambos equipos {equipoA} y {equipoB} recibira +1 puntos  ")
            for key,value in equipo.items():
                if str(key) == equipoA.upper():    
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    puntos=equipo[key].get("puntos Ganados")
                    puntos=(puntos+1)
                    empate=equipo[key].get("partidos Empatados")
                    empate=(empate+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesA)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesB)
                    k={
                        "partidos Jugados":jugados,
                        "puntos Ganados":puntos,
                        "partidos Empatados":empate,  
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(k)
                    break

                print(f"ok equipo {str(key)} {value} ") 

            for key,value in equipo.items():
                if str(key) == equipoB.upper():
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    puntos=equipo[key].get("puntos Ganados")
                    puntos=(puntos+1)
                    empate=equipo[key].get("partidos Empatados")
                    empate=(empate+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesB)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesB)
                    q={
                        "partidos Jugados":jugados,
                        "puntos Ganados":puntos,
                        "partidos Empatados":empate,
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(q)
                    break                          

        print(fecha)
    elif op==6:
        os.system('cls')
        print("aqui podras ver los datos mas relevantes del torneo \n1. Posicion en la tabla\n2. Equipos con mas Goles\n3. Los Equipos Mas goleados\n4. Salir ")
        ops=(int(input()))
        # equipo2 = sorted(equipo.items(), key=lambda x: getitem(x[1], "partidos Ganados"),reverse=True)
        # equipo3 =dict(equipo2)
        while isSortActive==True:

            if ops==1:
                equipo2 = sorted(equipo.items(), key=lambda x: getitem(x[1], "partidos Ganados"),reverse=True)
                equipo3 =dict(equipo2)
                print("Equipo         partidos Ganados        puntos Ganados")
                for key,value in equipo3.items():
                    print(  {equipo3[key]["nombre"].ljust(10)},format(str(equipo3[key]["partidos Ganados"])).rjust(9),str(equipo3[key]["puntos Ganados"]).rjust(19))
                    
                
                input("*****  Press Enter to Continue  ************")   
                break   
            elif ops==2:
                equipo2 = sorted(equipo.items(), key=lambda x: getitem(x[1], "goles A Favor"),reverse=True)
                equipo3 =dict(equipo2)
                print("Equipo         partidos Ganados        goles A Favor")
                for key,value in equipo3.items():
                    print(  {equipo3[key]["nombre"].ljust(10)},format(str(equipo3[key]["partidos Ganados"])).rjust(9),str(equipo3[key]["goles A Favor"]).rjust(19))
                   
                
                input("*****  Press Enter to Continue  ************")   
                break
            elif ops==3:
                equipo2 = sorted(equipo.items(), key=lambda x: getitem(x[1], "goles En Contra"),reverse=True)
                equipo3 =dict(equipo2)
                print("Equipo         partidos Perdidos        goles En Contra")
                for key,value in equipo3.items():
                    print(  {equipo3[key]["nombre"].ljust(10)},format(str(equipo3[key]["partidos Perdidos"])).rjust(9),str(equipo3[key]["goles En Contra"]).rjust(19))
                    


                input("*****  Press Enter to Continue  ************") 
                break   
            elif ops==4:
                rta=input("Desea Salir del programa S o N ")
                if rta.upper()=="S":
                    isSortActive=False
                elif rta.upper()=="N":
                    isSortActive=True
                
            
        

    elif op==7:
        print("Equipo en casa       Goles   Equipo visitante    Goles  ")
        for key,value in fecha.items():
            print(str(fecha[key]["Equipo en casa"]).ljust(9),str(fecha[key]["Goles"]).rjust(15),str(fecha[key]["Equipo visitante"]).rjust(13),str(fecha[key]["Goles visitante"]).rjust(12))
       
        input("*****  Press Enter to Continue  ************")
            # "Equipo en casa" : equipoA.upper(),
            # "Goles" :golesA,
            # "Equipo visitante" : equipoB.upper(),
            # "Goles visitante" : golesB

    elif op==8:
        rta=input("Desea Salir del programa S o N ")
        if rta.upper()=="S":
            isMenuActive=False
        elif rta.upper()=="N":
            isMenuActive=True