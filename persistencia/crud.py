import core as cr
import os
import time

def AddItemDicc():
            dicc={}
            dicDir={}
            os.system('cls')
            print("****************************************") 
            print("*                                      *")
            print("*¡   Registro de Contactos           ! *")
            print("*                                      *")
            print("****************************************")
            isAddItem=True
            while isAddItem==True:

                nombre=input("Nombre del contacto   : ")
                email=input("Email del contacto     : ")
                movil=input("Movil del contacto     : ")
                fechac=input("Fecha de cumpleaños   : ")
                os.system("pause")
                os.system('cls')
                print("****************************************") 
                print("*        ¡Registro de Direcciones!     *")
                print("****************************************")
                isAddDir=True
                while isAddDir==True:
                    valor=len(dicDir)
                    ciudad=input("Ingrese la Ciudad : ")
                    direccion=input("Ingrese la Direccion : ")
                    dicDir.update({valor:{"ciudad":ciudad,"direccion":direccion}})
                    rta=input("Desea ingresar otra Direccion S o N")
                    if rta.upper()=="S":
                        isAddDir=True
                    elif rta.upper()=="N":
                        isAddDir=False
                os.system("pause")
                os.system('cls')
                print("****************************************") 
                print("*        ¡Registro de Hobbies!         *")
                print("****************************************")
                isAddHob=True
                dicHob={}
                dicHob.clear()
                while isAddHob==True:
                    valor=len(dicHob)
                    hob=input("Ingrese el Hobbie : ")
                    dicHob.update({valor:{"hobbie":hob}})
                    rta=input("Desea ingresar otro Hobbie S o N")
                    if rta.upper()=="S":
                        isAddHob=True
                    elif rta.upper()=="N":
                        isAddHob=False   
                contacto={
                        "nombre":nombre,
                        "email":email,
                        "movil":movil,
                        "direcciones":dicDir,
                        "hobbies":dicHob
                    }
                cr.crearInfo("contacto.json", contacto)
                # agenda.append(contacto)
                rta=input("Desea ingresar otro contacto S o N")
                if rta.upper()=="S":
                    isAddItem=True
                elif rta.upper()=="N":
                    isAddItem=False
def VerData(data):
    os.system('cls')
    for item in data['data']:
        print(f"{item['nombre']}\t{item['email']}".expandtabs())
    v=input("Presione enter para continuar....")

def BuscarData(data):
    os.system('cls')
    indice=1
    print('-------------------------------------------------------------------')
    print(f"{'Item'.ljust(15)}|\t{'Nombre'.ljust(30)}|\t{'Email'.ljust(30)}".expandtabs())
    print('-------------------------------------------------------------------')
    for item in data['data']:
        print(f"{str(indice).ljust(15)}|\t{item['nombre'].ljust(30)}|\t{item['email'].ljust(30)}".expandtabs())
        indice=indice+1
    items=int(input("Digite el nro de contacto a editar"))

    for key,valor in data['data'][items-1].items():
        print(f"{key}:{valor}")
        modif=input('Desea modificar valor S o N :')
        if (modif.upper()=='S'):
            data['data'][items-1][key]=input("Ingrese un nuevo "+key+": ")
    
    cr.editarInfo('contacto.json',data)
    v=input("Presione enter para continuar....")
    

