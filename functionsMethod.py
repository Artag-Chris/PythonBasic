import json
def loadFile():
    with open("pokemonSaves/pokemons.json","r") as loadPokemons:
        c=loadPokemons.read()
        c=json.loads(c)
        return c
def firtsPoke(partyMember):
    with open("pokemonSaves/party.json","w")as party:
        json.dump(partyMember,party,indent=4)
        party.close()
def active():
   with open("pokemonSaves/party.json","r") as partyMemberA:
    active=partyMemberA.read()
    active=json.loads(active)    
    pokeA=active["Active"]
    return pokeA

def checkFile():
    try:
        with open('pokemonSaves/party.json', 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def AddToTeam(partyMember):
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

def showPokemons():
    with open("pokemonSaves/party.json","r") as show:
        party= show.read()
        party= json.loads(party)
        return party
def movePokemons():
    with open("pokemonSaves/party.json","r") as move:
        move= move.read()
        move= json.loads(move)
        return move
def organizarParty(*arg):
    with open("pokemonSaves/party.json", "w") as org:
        org.seek(0)
        json.dump(arg,org,indent=4)