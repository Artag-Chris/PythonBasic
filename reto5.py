import json
import os
import random
import functionsMethod
#usar Try y error 
#mejorar front-end
#mejorar menu de opciones 
isMenuActive=True
op=0
ops=0

with open("pokemonSaves/pokemons.json","r") as loadPokemons:
    c=loadPokemons.read()
    c=json.loads(c)
os.system('cls')
print("********************************************")
print("***                                    *****")
print("**  Pokemon Python Simulator beta      *****")
print("***                                    *****")
print("********************************************")
input("*****  Press Enter to Continue  ************")
while isMenuActive==True:
    os.system('cls')
    print("Hi this is a pokemon demo for file management practice")
    print("if you want to select your first pokemon press ***1***")
    print("you can try to Catch another pokemon with Option *2***")
    print("here yo can See your Pokemons Stats and Moves ****3***")
    print("and here you can leave this Demo *****************4***")
    op=int(input())
    if op==1:
        os.system('cls')
        print("For this demo I recomend to choose Pikachu for your first Pick")
        print("Name            lv         attacks")
        for key,value in c.items():

            print(str(c[key]["Name"]).ljust(15),str(c[key]["stats"]["Level"]).ljust(10),c[key]["attacks"])

        print("1 for Pikachu 2 for Bulbasaur 3 for Charmander")
        selected=int(input("Which pokemon Do you like to choose ?"))
        if selected==1:
            picked=c["first"]
            partyMember={"Active":picked}
            picked=partyMember["Active"]["Name"]
            print(f"You selected {picked} Congratulations!!")
            functionsMethod.firtsPoke(partyMember)
            os.system("pause")
            input("*****  Press A to Continue  ************")        
        elif selected==2:
            picked=c["second"]
            partyMember={"Active":picked}
            picked=partyMember["Active"]["Name"]
            print(f"You selected {picked} Congratulations!!")
            os.system("pause")
            functionsMethod.firtsPoke(partyMember)
            input("*****  Press A to Continue  ************")
        elif selected==3:
            picked=c["third"]
            partyMember={"Active":picked}
            picked=partyMember["Active"]["Name"]
            print(f"You selected {picked} Congratulations!!")
            functionsMethod.firtsPoke(partyMember)
            os.system("pause")
            input("*****  Press A to Continue  ************")
        else:
            print("Not valid input")
            os.system("pause")
            input("*****  Press A to Continue  ************")   
    elif op==2:
        os.system('cls')
        print("Te adentras a Viridian Forest y encuentras un pokemon salvaje ")
        if functionsMethod.checkFile()==False:
            print("Pero no tienes un Pokemon para una batalla asi que huyes")
            input("*****  Press A to Continue  ************")
        else:
            c=functionsMethod.loadFile()
            enemy=random.randrange(1, 4)
            print(enemy)
            if enemy==1:
                pokeB=c["first"]
                nameW=pokeB["Name"]
                print(F"A wild {nameW} appears")
            elif enemy==2:
                pokeB=c["second"]
                nameW=pokeB["Name"]
                print(F"A wild {nameW} appears")
            elif enemy==3:
                pokeB=c["third"]
                nameW=pokeB["Name"]
                print(F"A wild {nameW} appears")
            else:
                print("not valid option")
        input("*****  Press A to Continue  ************")
        pokeA=functionsMethod.active()
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
                print("********************************************")
                print(f"***  1 {a}       2 {b}     ")
                print("********************************************")
                print(f"***  3 {c}          4 {d}     ******")
                print("********************************************")
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
                   winner=x
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
                if hpA<=0 or hpA<-0:
                   winner=y
                   break
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
                if hpA<=0 or hpA<-0:
                   winner=y
                   break
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
                if hpB<=0 or hpB<-0:
                   winner=x
                   break
                
                   hpA=int(0)
                input("*****  Press A to Continue  ************")
            elif speedA == speedB:
                speedTie=random.randrange(1, 3)
                if speedTie==1:
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
                       winner=x
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
                    if hpA<=0 or hpA<-0:
                       winner=y
                       break
                    input("*****  Press A to Continue  ************")
                if speedTie==2:
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
                        if hpA<=0 or hpA<-0:
                           winner=y
                           break
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
                        if hpB<=0 or hpB<-0:
                           winner=x
                           break
                        
                           hpA=int(0)
                        input("*****  Press A to Continue  ************")


        print(f"the winner is !!! {winner} ")
        os.system("pause")
        print(f"Would you like to cath {y} ? ")
        catch=input(" Y for yes N for no")
        if catch.upper()=="Y":
            newPoke=pokeB
            
            
            with open("pokemonSaves/party.json","r") as partyMemberA:
                active=partyMemberA.read()
                active=json.loads(active)
            length= len(active)+1      
            partyMember={length:newPoke}
            print(length)
            #con este method puedo leer un archivo y escribirlo
            functionsMethod.AddToTeam(partyMember)
            print(active)
        elif catch.upper()=="N":
            print(f"The {y} runs Away, he was really sad")
        
        else:
            print("not valid input")

        input("*****  Press A to Continue  ************")
    
    elif op==3:
        if functionsMethod.checkFile()==False:
            print("Pero no tienes un Pokemon para ver")
            input("*****  Press A to Continue  ************")
        else:
            party=functionsMethod.showPokemons()
            party2=dict(party)
            #print(party2)
            print("Nombre         level        stats")
            for key, value in party.items():
                print(str(party2[key]["Name"]).ljust(15),str(party2[key]["stats"]["Level"]).ljust(10),party2[key]["stats"])
            
            input("*****  Press A to Continue  ************")

        print("Would you like to Change your Active Pokemon? ")
        print("if you have 4 or more pokemons you can delete 1")
        change=input("Y for yes N for no ")
        if change.upper()=="N":
            print("Leaving...")
            input("*****  Press A to Continue  ************")
        elif change.upper()=="Y":
            party=functionsMethod.showPokemons()
            size=len(party)
            print(size)
            if size==1:
                print("You cannot change Pokemon to Active")
            elif size==2:
                resp=functionsMethod.movePokemons()
                resp=resp["Active"]
                #print(resp)
                b=party["2"]
                party["Active"].update(b)  
                party["2"].update(resp)
                print(party)
                functionsMethod.AddToTeam(party)
            elif size==3:
                resp=functionsMethod.movePokemons()
                resp=resp["Active"]
                x=resp["Name"]
                b=party["2"]
                y=b["Name"]
                c=party["3"]
                z=c["Name"]
                switch=int(input(f"tu pokemon Activo es {x} oprime 1 para que {y} este Activo o 2 para {z} "))
                if switch==1:
                    party=functionsMethod.showPokemons()
                    resp=functionsMethod.movePokemons()
                    resp=resp["Active"]
                    party["Active"].update(b) 
                    party["2"].update(resp)
                    #print(party)
                    functionsMethod.AddToTeam(party)
                    input("*****  Press A to Continue  ************")
                elif switch==2:
                    party=functionsMethod.showPokemons()
                    resp=functionsMethod.movePokemons()
                    resp=resp["Active"]
                    party["Active"].update(c) 
                    party["3"].update(resp)
                    functionsMethod.AddToTeam(party)
                    input("*****  Press A to Continue  ************")
                else:
                    print("option not valid")
            elif size>=4:
                resp=functionsMethod.movePokemons()
                resp=resp["Active"]
                x=resp["Name"]
                b=party["2"]
                y=b["Name"]
                c=party["3"]
                z=c["Name"]
                d=party["4"]
                xx=d["Name"]
                print("El Pokemon Active no se podra borrar  ")
                switch=int(input(f"tu pokemon Activo es {x} oprime 1 para liberar a {y} \n2 para {z} 3 para {xx} "))
                if switch==1:
                    
                    party["2"].update(c)
                    party["3"].update(d)
                    party.pop("4")
                    print(party)
                    functionsMethod.firtsPoke(party)
                    input("*****  Press A to Continue  ************")
                elif switch==2:
                    party["3"].update(d)
                    party.pop("4")
                    print(party)
                    functionsMethod.firtsPoke(party)
                    input("*****  Press A to Continue  ************")
                elif switch==3:
                    party.pop("4") 
                    #party["3"].update(resp)
                    print(party)
                    functionsMethod.firtsPoke(party)
                    input("*****  Press A to Continue  ************")
                    print("The pokemon is now free")

                

    elif op==4:
            print("Do you want to quit? all your Pokemons will be save don`t worry")
            quit=input(" Y for yes N for No")
            if quit.upper()=="Y":
                isMenuActive=False
            elif quit.upper()=="N":
                isMenuActive=True
            else:
                print("invalid option")


            

