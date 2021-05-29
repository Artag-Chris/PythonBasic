ValorCredito = float(input("escriba el valor del credito "))
ValorInteresAnual = 0.13
TiempoDelCredito = float(input("escriba el tiempo de meses a pagar "))
ValorInteresMensual= ValorInteresAnual/12

i=1
CuotaSinInteres = 0
Interes = (ValorCredito*ValorInteresAnual)/12
print(Interes)
CuotaFija = (ValorCredito* (ValorInteresMensual * (1 + ValorInteresMensual)** TiempoDelCredito)) / (((1 + ValorInteresMensual)** TiempoDelCredito) - 1)
print(CuotaFija)
while i <= TiempoDelCredito:
    print(i)
    Interes = (ValorCredito*ValorInteresAnual)/12
    print(f" estos son los intereses {Interes}")
    CuotaSinInteres = (CuotaFija - Interes)
    print(f" este es el valor de la cuota sin interes {CuotaSinInteres}")
    ValorCredito = (ValorCredito - CuotaFija + Interes) 
    print(f" este es el valor en que queda el credito {ValorCredito}")
    i +=1

    
