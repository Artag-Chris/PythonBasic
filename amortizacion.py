MontoDelPrestamo = 20000000
PorcentajeAnual = 13
tiempo = 10
ValorInteresAnual = PorcentajeAnual/100
ValorInteresMensual= ValorInteresAnual/12
Interes = (MontoDelPrestamo*ValorInteresAnual)/12
CuotaFija = (MontoDelPrestamo* (ValorInteresMensual * (1 + ValorInteresMensual)** tiempo)) / (((1 + ValorInteresMensual)** tiempo) - 1)
print(round(Interes,2))
print(round(CuotaFija,2))

i=1

while i <= tiempo:
    print(i)
    Interes = (MontoDelPrestamo*ValorInteresAnual)/12
    print(f" estos son los intereses {round(Interes)}")
    CuotaSinInteres = (CuotaFija - Interes)
    print(f" este es el valor de la cuota sin interes {round(CuotaSinInteres)}")
    print(f" el valor de su cuota fija es de {round(CuotaFija)} ")
    MontoDelPrestamo = (MontoDelPrestamo - CuotaFija + Interes) 
    print(f" este es el valor en que queda el credito {round(MontoDelPrestamo,2)}")
    i +=1
