Pereira = []
Bucaramanga = []
Bogota = []
Cali = []
Barranquilla = []
"""
def Note1  (array):
    sum = 0
    for element in array:
        sum += element / 2
    return sum 
"""


a = float(input("ingrese la temperatura de pereira "))
Pereira.append(a)
b = float(input("ingrese la  2da temperatura de pereira "))
Pereira.append(b)
c = (a + b)/2
Pereira.append(c)
del Pereira[0]
del Pereira[0]
print(Pereira)

d = float(input("ingrese la temperatura de Bucaramanga "))
Bucaramanga.append(d)
e = float(input("ingrese la  2da temperatura de Bucaramanga "))
Bucaramanga.append(e)
print(Bucaramanga)
f = (d + e)/2
Bucaramanga.append(f)
del Bucaramanga[0]
del Bucaramanga[0]
print(Bucaramanga)

g = float(input("ingrese la temperatura de Bogota "))
Bogota.append(g)
h = float(input("ingrese la  2da temperatura de Bogota "))
Bogota.append(h)
i = (g + h)/2
Bogota.append(i)
del Bogota[0]
del Bogota[0]
print(Bogota)

j = float(input("ingrese la temperatura de Cali "))
Cali.append(g)
k = float(input("ingrese la  2da temperatura de Cali "))
Cali.append(h)
l = (j + k)/2
Cali.append(l)
del Cali[0]
del Cali[0]
print(Cali)

m = float(input("ingrese la temperatura de Barranquilla "))
Barranquilla.append(g)
n = float(input("ingrese la  2da temperatura de Barranquilla "))
Barranquilla.append(h)
o = (m + n)/2
Barranquilla.append(o)
del Barranquilla[0]
del Barranquilla[0]
print(Barranquilla)

if Pereira > Bucaramanga and Pereira > Bogota and Pereira > Cali and Pereira > Barranquilla:
    print(f"Pereira es la mas caliente su temperatura promedio es de {Pereira} grados")
elif Cali > Pereira and Cali > Bucaramanga and Cali > Bogota and Cali > Barranquilla:
    print(f"cali es la mas caliente su temperatura promedio es de {Cali} grados")
elif Bucaramanga > Pereira and Bucaramanga > Cali and Bucaramanga > Bogota and Bucaramanga > Barranquilla:
    print(f"Bucaramanga es la mas caliente su temperatura promedio es de {Bucaramanga} grados")
elif Bogota > Pereira and Bogota > Cali and Bogota > Bucaramanga and Bogota > Barranquilla:
    print(f"bogota es la mas caliente su temperatura promedio es de {Bogota} grados")
elif Barranquilla > Pereira and Barranquilla > Cali and Barranquilla > Bogota and Barranquilla > Bucaramanga:
    print(f"Barranquilla es la mas caliente su temperatura promedio es de {Barranquilla} grados")
else:
    print(f"error al calculcar") 

if Pereira < Bucaramanga and Pereira < Bogota and Pereira < Cali and Pereira < Barranquilla:
    print(f"Pereira es la mas fria su temperatura promedio es de {Pereira} grados")
elif Cali < Pereira and Cali < Bucaramanga and Cali < Bogota and Cali < Barranquilla:
    print(f"cali es la mas fria su temperatura promedio es de {Cali} grados")
elif Bucaramanga < Pereira and Bucaramanga < Cali and Bucaramanga < Bogota and Bucaramanga < Barranquilla:
    print(f"Bucaramanga es la mas fria su temperatura promedio es de {Bucaramanga} grados")
elif Bogota < Pereira and Bogota < Cali and Bogota < Bucaramanga and Bogota < Barranquilla:
    print(f"bogota es la mas fria su temperatura promedio es de {Bogota} grados")
elif Barranquilla < Pereira and Barranquilla < Cali and Barranquilla < Bogota and Barranquilla < Bucaramanga:
    print(f"Barranquilla es la mas fria su temperatura promedio es de {Barranquilla} grados")
else:
    print(f"error al calculcar")