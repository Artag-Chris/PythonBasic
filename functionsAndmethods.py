def resta(a,b,c=0):
    if c <0:
        print((a-b)*c)
    else:
        print(a-b)
resta(10, 8)

def verLista(lista):
    for item in lista:
        print(item, end=" ")

verLista(["rojo", "azul"])

#el ** se usa para decir que algo es dinamico y se usa tambien para indicar que el parametro es un diccionario
def verLista(**lista):
    for key, value in lista.items():
        print(f"{key} : {value} ", end="\n")

diccionario={"nombre" :"jose ", "edad" : 14}

verLista(**diccionario)

def divicion(numerador,dividiendo):
    """
    esta funcion permitedividir dos numeros diferentes a cero
    """
    if dividiendo==0:
        return
    else:
        return numerador/dividiendo
print(divicion.__doc__)
resultado=divicion(8,3)
if resultado !=None:
    print(resultado)
else:
    print("error al dividir")


def valores(*args):
    for i in args:
        print(f" {i}  " ,end=" ")

valores(1,2,3,4,5,"chris",[1.2,2.3,"alejandro"], 6,7,8,9,{"perro" : "husky", "diccionario2": {"perro" : "siberian"}}, 10,11 )
def swap(listat, x, y):
    temp=listat[x]
    listat[x] = listat[y]
    listat[y] = temp

def selectionSort(aList):
    for i in range(len(aList)):
        print(i)
        least = i
        for k in range(i+1,len(aList)):
            if aList[k] < aList[least]:
                least=k

            swap(aList,least,i)

print(selectionSort(valores))