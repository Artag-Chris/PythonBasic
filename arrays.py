array = ([[1,2,3], [4,5,6], [7,8,9]])
"""
asi se agregan los datos en una matriz
array[0][0]=3
array[0][1]=2
array[0][2]=1
"""
#usare la siguente variable para indicar la posicion en un array
Pos = -1


"""
for i in array :
    print(i)
    en python se usan dos bucles for para recorrer una matriz
"""


for i in range(len(array)):
    for j in range(len(array[i])):
        print(array[i][j], end=" ")
    print()

"""
uno = float(input("primera nota  "))
dos = float(input("segunda nota  "))
tres = float(input("tercera nota  "))
arg = [uno,dos,tres]
print(arg)
"""

"""
def sumar(arg):
    if arg == []:
       suma = 0
    else:
        return arg[0] + sumar(arg[1:])
         
sumar(arg)
print(sumar(arg))
arg = [1, 2, 3, 4, 5]

def sumar (lista):
    suma = 0
    for elemento in lista:
        suma += elemento / 3
    return suma

print(sumar(arg))
"""

arry=[1,2,3]
for i in arry:
    print(f"el valor de i es {i}")


# con este loop se puede buscar en una array 
NewArray = [1,2,3,4,5,6,7,8,9]
element = int(input("que numero del 1 al 9 buscas?  "))
element2 = 8
flag = 0
"""
for i in NewArray:
    if (element==9):
       print("element found")
       flag= 1
       

       break
#break evita que sea infinito el codigo 
if (flag==0):
    print("element not found")
#in hace referencia adentro de una array
if (element2 in NewArray):
    print("element found")
else:
    print("element not found")



print(f" el elemento esta en la posicion {Pos} ")
"""
#este loop esta muy bien programado  estudiarlo 
def Search(NewArray):
    for n in range(0,len(NewArray)):
        if NewArray[n] == element:
           print(f"{NewArray[n]} at position {n} ")
      #  else:
          # print("element not found")

Search(NewArray)
