inventario=[]
prov=[]
compras=[]
isActivateMenu=True
isAddProducto=True
isAddProveedor=True
op=0
while isActivateMenu==True:
    print("1.Ingresar Producto\n2.Ingresar Proveedor\n3.Ver proveedor por producto\n4.Comprar\n5.Listar Productos\n6.Calcular compra total\n7.Salir")
    op=int(input())
    if op==1:
        isAddProducto=True
        while isAddProducto==True:
            codigo=input("Ingrese el codigo del producto :")
            nombre=input("Ingrese el nombre del producto :")
            valor=float(input("Ingrese el valor del producto : "))
            disponible=0
            producto=[codigo.upper(),nombre.upper(),disponible,valor,[]]
            inventario.append(producto)
            rta=input("Desea Ingresar otro producto S o N : ")
            if rta.upper()=="S":
                isAddProducto=True
            elif rta.upper()=="N":
                isAddProducto=False
            else:
                print("Respuesta no valida")
                isAddProducto=True
    elif op==2:
        palabra=input("Ingrese el codigo del producto a Buscar : ")
        isAddProveedor=True
        prov=[]
        for item in inventario:
            if palabra.upper() in item:
                while isAddProveedor==True:
                    idprov=input("Ingrese Identificacion Prov : ")
                    nombrep=input("Ingrese Nombre Prov : ")
                    ciudad=input("Ingrese ciudad Prov : ")
                    prov.append([idprov,nombrep,ciudad])
                    rta=input("Desea Ingresar otro proveedor S o N : ")
                    if rta.upper()=="S":
                        isAddProveedor=True
                    elif rta.upper()=="N":
                        isAddProveedor=False
                    else:
                        print("Respuesta no valida")
                        isAddProveedor=True
                item[4].extend(prov)
                    
    elif op==3:
        palabra=input("Ingrese el codigo del producto a Buscar : ")
        for producto in inventario:
            if palabra.upper() in producto:
                for prov in producto[4]:
                    print(f"Id Proveedor : {prov[0]} | Nombre Proveedor : {prov[1]}",end="\n")
                
    elif op==4:
        isBuying=True
        while isBuying==True: 
            palabra=input("Ingrese el codigo del producto a Comprar : ")
            cantidad=int(input("Ingrese Cantidad a Comprar : "))
            provid=input("Ingrese el codigo del Proveedor : ")
            valorc=float(input("Ingrese Cantidad a Comprar : "))
            isFound=False
            for producto in inventario:
                if palabra.upper() in producto:
                    for prov in producto[4]:
                        if provid in prov:
                            isFound=True
                    if isFound==True:
                        buy=([producto[0],producto[1],cantidad,valorc,provid])
                        if producto[3]!=valorc:
                            producto[3]=valorc
                        compras.append(buy)
                    else:
                        print("No se puede comprar")
            rta=input("Desea registrar otra compra S o N")
            if rta.upper()=="S":
                isBuying=True
            else:
                isBuying=False          
    elif op==5:
        for item in inventario:
            print(f"Codigo : {item[0]} Nombre Producto: {item[1]} Cantidad Disponible : {item[2]} Valor Unitario : {item[3]}",end="\n")
    elif op==6:
        totalcompra=0
        header=["Codigo","Nombre del producto","Cantidad","Valor Unit","Subtotal"]
        print(f"{header[0]} {header[1]} {header[2]} {header[3]} {header[4]}")
        for buy in compras:
            print(f"{buy[0].ljust(6)} {buy[1].ljust(19)} {str(buy[2]).ljust(8)} {str(buy[3]).ljust(10)} {(buy[2]*buy[3])}",end="\n")
            totalcompra=totalcompra+(buy[2]*buy[3])
        print(f"Total de la Compra : {totalcompra}")      
    elif op==7:
        rta=input("Desea Abandonar el Programa S o N : ")
        if rta.upper()=="S":
            isActivateMenu=False
        elif rta.upper()=="N":
            isActivateMenu=True
        else:
            print("Respuesta no valida")
            isActivateMenu=True
            
