import os
import time
#hacerle los cambios adecuados 
equipo={}
fecha={}
isMenuActive=True
isAddItem=True
partidosJugados=int(0)
partidosGanados=int(0)
partidosEmpatados=int(0)
partidosPerdidos=int(0)
golesAFavor=int(0)
golesEnContra=int(0)


isAddItem
op=0
while isMenuActive==True:
    print("1. Agregar equipo\n2. Ver equipo\n3. Agregar jugador\n5 Ingresar fecha\n7. Salir")
    op=(int(input()))
    print(op)
    if op==1:
        isAddItem=True
        while isAddItem==True:
            idEquipo=input("Id del equipo : ")
            nombre=input("Nombre del equipo : ")
            
            value={
                "nombre": nombre.upper(),
                "partidos Jugados": int(partidosJugados),
                "partidos Ganados": int(partidosGanados),
                "partidos Empatados": int(partidosEmpatados),
                "partidos Perdidos": int(partidosPerdidos),
                "goles A Favor": int(golesAFavor),
                "goles En Contra": int(golesEnContra),
                "jugadores":{}
            }
            equipo.update({idEquipo.upper():value})
            print(equipo)
            rta=input("Desea ingresar otro equipo S o N")
            if rta.upper()=="S":
                isAddItem=True
            elif rta.upper()=="N":
                isAddItem=False
    elif op==2:
        #equipo.update(data)
        print(equipo)
        
            
    elif op==3:   
        palabra=input("Ingrese Id a buscar : ")
        #los diccionarios se recorren por key" llave" y value"valor" en el nombre del directorio con el .items
        #ese valorc es una variable de contador para los value "valores podria tener cualquier nombre" va cambiando de valor 
        for key, valorc in equipo.items():
            #si la key "llave" es igual a palabra(input) hace lo siguiente
            if str(key) == palabra.upper():
                #este valor toma un numero que es la longitud que tiene el value de "ubicacion" si esta vacio sera 0
                valor=len(valorc["jugadores"])
                nombreJugador=input("Ingrese nombre del Jugador para registrar : ")
                posicion=input("Ingrese posicion para registrar : ")
                #aqui encuentra "jugadores" dentro del diccionario y le hace un update le agrega la nueva data
                valorc["jugadores"].update({valor:{"nombre del jugador" : nombreJugador, "posicion del jugador" : posicion}})
                
    elif op==5:
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
                if equipoA.upper() in equipo:
                    
                    jugados=equipo[key].get("partidos Jugados")
                    jugados= (jugados+1)
                    ganados=equipo[key].get("partidos Ganados")
                    ganados=(ganados+1)
                    golesMas=equipo[key].get("goles A Favor")
                    golesMas=(golesMas+golesA)
                    golesMenos=equipo[key].get("goles En Contra")
                    golesMenos=(golesMenos+golesB)
                    k={
                        "partidos Jugados":jugados,
                        "partidos Ganados":ganados,
                        "partidos Empatados":+0,
                        "partidos Perdidos":+0,
                        "goles A Favor": golesMas,
                        "goles En Contra" :golesMenos
                    }
                    equipo[key].update(k)
                    print(f"ok equipo {str(key)} {value} ")
                        
                  
                        
                   

        print(fecha)

    elif op==7:
        rta=input("Desea Salir del programa S o N ")
        if rta.upper()=="S":
            isMenuActive=False
        elif rta.upper()=="N":
            isMenuActive=True