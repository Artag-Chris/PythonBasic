import json
import os
import random
import functionsMethod

#primer numero incluido segundo numero no incluido
#metodo random
#print(random.randrange(0, 4))
#se necesita importar json para usar su dump
# pokemons={
#     "first":{
#         "Name":"Pikachu",
#         "attacks":["ThunderShock","Quick Attack","fly","Energy Ball"],
#         "stats":{
#             "Level":20,
#             "Health Points":35,
#             "Attack":28,
#             "Defence":17,
#             "Special Attack":31,
#             "Special Defence": 27,
#             "Speed": 33
#         }
#     },
#     "second":{
#         "Name": "Bulbasaur",
#         "attacks":["Vine Whip","Seed Bomb","Double-Edge","Sweet Scent"],
#         "stats":{
#             "Level":20,
#             "Health Points": 30,
#             "Attack": 17,
#             "Defence": 20,
#             "Special Attack": 30,
#             "Special Defence": 25,
#             "Speed":25
#         }
#     },
    
#     "third" : {
#         "Name": "Charmander",
#         "attacks":["Ember","Dragon Breath","Slash","Thunder Punch"],
#         "stats":{
#             "Level":20,
#             "Health Points": 33,
#             "Attack": 29,
#             "Defence": 15,
#             "Special Attack": 20,
#             "Special Defence": 25,
#             "Speed":30
#     }
#     },
# }   

#con el with es mas facil usar open por que no necesita usar una variable
#el as eso como un alias para no escribir todo de nuevo
#with open("pokemons.json","w")as poke:
    #el json.dump es para escribir diccionarios en archivos .json u otro
    #recibe tres parametros 
    #1 diccionario que se va a escribir
    #2 el As de arriba como el alias
    #3 la indentacion para que el .json se vea presentable
    #4 y tambien podria usar un sort=True esto es recomendable hacerlo
    #json.dump(pokemons,poke,indent=4)
    #poke.close()

os.system("cls")

with open("pokemonsaves/pokemons.json","r") as readPoke:
    c=readPoke.read()
    c=json.loads(c)
    #print(c)   
    print("Name            lv         attacks")
    for key,value in c.items():
       
        print(str(c[key]["Name"]).ljust(15),
        str(c[key]["stats"]["Level"]).ljust(10),
        c[key]["attacks"])
    
    print("1 for Pikachu 2 for Bulbasaur 3 for Charmander")
    selected=int(input("Which pokemon Do you like to choose ?"))
    if selected==1:
        picked=c["first"]
        partyMember={"Active":picked}
        picked=partyMember["Active"]["Name"]
        print(f"You selected {picked} Congratulations!!")
        functionsMethod.firtsPoke(partyMember)
            
    elif selected==2:
        picked=c["second"]
        partyMember={"Active":picked}
        print(f"You selected {picked} Congratulations!!")
        functionsMethod.firtsPoke(partyMember)
        
    elif selected==3:
        picked=c["third"]
        partyMember={"Active":picked}
        print(f"You selected {picked} Congratulations!!")
        functionsMethod.firtsPoke(partyMember)
    else:
        print("Not valid input") 

enemy=random.randrange(1, 4)
print(enemy)
if enemy==1:
    pokeB=c["first"]
    print(pokeB)
elif enemy==2:
    pokeB=c["second"]
    print(pokeB)
elif enemy==3:
    pokeB=c["third"]
    print(pokeB)
else:
    print("not valid option")

#aqui comienzan las peleas    

with open("pokemonSaves/party.json","r") as partyMemberA:
    active=partyMemberA.read()
    active=json.loads(active)    
    pokeA=active["Active"]
    
    hpA=pokeA["stats"]["Health Points"]
    hpB=pokeB["stats"]["Health Points"]
    speedA=pokeA["stats"]["Speed"]
    speedB=pokeB["stats"]["Speed"]
    

    while hpA>int(0) or hpB>int(0):
        
        #si A tiene mas Velocidad que B ataca primero
        if speedA > speedB:
            x=pokeA["Name"]
            y=pokeB["Name"]
            print(f"What {x} will do? ")
            #aqui vuelvo la lista de ataques que estaba dentro del directorio en variables para selecionarlas mas facil
            a=pokeA["attacks"][0]
            b=pokeA["attacks"][1]
            c=pokeA["attacks"][2]
            d=pokeA["attacks"][3]
            #mini menu de seleccionar ataque
            print(f"1**{a}** 2**{b}** \n3**{c}**4**{d}** ")
            ops=int(input())
            print(f"{x} used")
            print(pokeA["attacks"][ops-1])
            attA=pokeA["stats"].get("Special Attack")
            print(f"Dealt {attA} Damage")
            input("*****  Press A to Continue  ************")
            defB=pokeB["stats"].get("Defence")
            result=(attA-defB)
            print(f"{y} with {defB} Defence only took {result} Damage")
            hpB=(hpB-result)
            print(f"{y} only has {hpB} Health Points remain ")
            #aqui si el hp del pokemon B llega a 0 o menor rompe el ciclo
            if hpB<=0 or hpB<-0:
                break
                hpB=int(0)
           
            

            #aqui es el turno del enemigo que usara ataques al random
            print(f"{y} used ")
            f=pokeB["attacks"][0]
            g=pokeB["attacks"][1]
            h=pokeB["attacks"][2]
            i=pokeB["attacks"][3]
            opsB= random.randrange(0, 4)
            print(pokeB["attacks"][opsB])
            attcB=pokeB["stats"].get("Attack")
            print(f"{y} Dealts {attcB} Damage ")
            defA=pokeA["stats"].get("Defence")
            resultB=(attcB-defA)
            print(f"{x} with {defA} Defence, only took {resultB} Damage ")
            input("*****  Press A to Continue  ************")
            
        #oponente ataca primero
        elif speedA < speedB:
            #turno del oponente
            y=pokeB["Name"]
            x=pokeA["Name"]
            print(f"{y} used ")
            f=pokeB["attacks"][0]
            g=pokeB["attacks"][1]
            h=pokeB["attacks"][2]
            i=pokeB["attacks"][3]
            opsB= random.randrange(0, 4)
            print(pokeB["attacks"][opsB])
            attcB=pokeB["stats"].get("Attack")
            print(f"{y} Dealts {attcB} Damage ")
            defA=pokeA["stats"].get("Defence")
            resultB=(attcB-defA)
            print(f"{x} with {defA} Defence, only took {resultB} Damage ")
            input("*****  Press A to Continue  ************")
            #turno jugador
            print(f"What {x} will do? ")
            #aqui vuelvo la lista de ataques que estaba dentro del directorio en variables para selecionarlas mas facil
            a=pokeA["attacks"][0]
            b=pokeA["attacks"][1]
            c=pokeA["attacks"][2]
            d=pokeA["attacks"][3]
            #mini menu de seleccionar ataque
            print(f"1**{a}** 2**{b}** \n3**{c}**4**{d}** ")
            ops=int(input())
            print(f"{x} used")
            print(pokeA["attacks"][ops-1])
            attA=pokeA["stats"].get("Special Attack")
            print(f"Dealt {attA} Damage")
            input("*****  Press A to Continue  ************")
            defB=pokeB["stats"].get("Defence")
            result=(attA-defB)
            print(f"{y} with {defB} Defence only took {result} Damage")
            hpA=(hpA-result)
            print(f"{y} only has {hpA} Health Points remain ")
            if hpA<=0 or hpA<-0:
                break
                hpA=int(0)
        

    print(f"the winner is {x} ")
    print(f"would you like to catch {y}? Y or N  ")
   
    newPoke=pokeB
    length= len(active)+1
    print(length)
    partyMember={"New":newPoke}
    #con este method puedo leer un archivo y escribirlo
    with open("pokemonSaves/party.json","r+") as party:
        #leo el archivo en party.json
        active=party.read()
        #aqui convierto esa informacion a un diccionario
        active=json.loads(active)
        #aqui le hago un update a active que es el diccionario base completo y le sumo el nuevo pokemon
        active.update(partyMember)
        print(active)
        #este seek se para en la posicion 0 de todo el archivo y reescribe desde hay
        party.seek(0)
        #aqui se escribe al archivo .json terminando el proceso de añadir pokemons al party
        json.dump(active,party,indent=4)


    


