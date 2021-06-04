##isValid=False;
##while isValid==False:
##    try:
##        edadF = int(input("Ingrese la edad :"))
##    except ValueError:
##        print('ValueError: El valor ingresado no se puede convertir a entero')
##    else:
##        print('Edad Aceptada')
##        isValid=True
    
###Creacion de una lista
##materias=["Calculo"]
###Imprimir lista
##print (materias)
###Imprimir Elemento de una Lista
##print (materias[0])
###Creacion de una Lista Vacia
##alumnos=[]
##print (alumnos)
#----------------------------
##nombre=input("Ingrese el Nombre : ")
##edad = int(input("Ingrese la edad :"))
##persona=[nombre,edad]
##print(persona)
#----------------------------
##agenda=[]
##for i in range(1,3):
##    nombreF=input("Ingrese el Nombre : ")
##    edadF = int(input("Ingrese la edad :"))
##    personaF=[nombreF,edadF]
##    agenda.append(personaF)
##print (agenda)
#-----------------------------
##num_list = [1,2,3,4,5,7]
##print(f'Numeros en la  Lista {num_list}')
##num = int(input("Ingrese un numero a agregar en la lista:\n"))
##index = int(input(f'Por favor ingrese un numero entre 0 and {len(num_list) - 1}\nPara agregalo a la lista:\n'))
##num_list.insert(index, num)
##print(f'Numeros actualizados List {num_list}')
#-----------------------------
##list_num = []
##list_num.extend([1, 2])  # extending list elements
##print(list_num)
##list_num.extend((3, 4))  # extending tuple elements
##print(list_num)
##list_num.extend("ABC")  # extending string elements
##print(list_num)
#-----------------------------
##pares = [2, 4, 6]
##impares = [1, 3, 5]
##nums = pares + impares
##print(nums)
##print(nums[4])
##print(nums[-4])
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(letras)
del letras[4]
print(letras)
del letras[1:4]
print(letras)
try:
    del letras
    print(letras)
except NameError:
    print('ValueError: La lista no existe')
else:
    print('Lista mostrada')


           
