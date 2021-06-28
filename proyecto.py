import json
import os
import time
factura={}
electricidad={}
agua={}
cable={}
gas={}
mercado={}

def checkFile():
    try:
        with open("factura.json", 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def crearInfo(*dict):
    with open("facturas.json","w") as write:
        json.dump(dict,write,indent=4)
        write.close()




isMenuActivate=True
while isMenuActivate==True:
    os.system("cls")
    print("*****************************************") 
    print("*                                      **")
    print("*  Bienvenidos a Gestor de facturas    **")
    print("*                                      **")
    print("*****************************************")
    input("*****  Press Enter to Continue  *********")
    os.system('cls')
    print("Aqui podras registrar y tener un control de todas tus facturas")
    print(" Elige una opcion \n1 Registrar factura de Electricidad ")
    op=int(input())
    if op==1:
        print("ok")
        mes=input("ingresa el mes de la factura de la electricidad ")
        valor=int(input("ingresa el valor de la factura "))
        value=len(electricidad)
        elect={
            mes:valor
        }
        electricidad.update({value:elect})
        factura.update({"luz":electricidad})
        print(factura)
        #crearInfo(factura)
        #electricidad.clear()
        c=checkFile("factura.json")
        print(c)
        input("*****  Press Enter to Continue  *********")