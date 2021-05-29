#lista principal
inventario=[]
#lista para proveedores
prov=[]
#lista del seguimiento de venta
vent=[]
#menu principal, es el de navegacion 
isActiveMenu=True
#menu de producto
isAddProduct=True
#menu de proveedores se pueden ingresar mas de un proveedor distinto del mismo producto
isAddProveedor=True
#menu de registro de venta 
isAddBuy=True
#opcion  basica que sera un input para la navegacion 
option=0
while isActiveMenu==True:
    #se coloco isAddProduct=True por que sin esto no deja entrar al menu opcion 1
    isAddProduct=True
    print("1. Ingresar producto\n2. Ingresar Proveedor\n3. Comprar\n4. Listar Productos\n5. Salir")
    option=int(input())
    #aqui se suman los productos a la lista principal y se les da un id principal para facilitar busqueda
    if option==1:
        while isAddProduct==True:
            codigo=input("Ingrese el codigo del producto : ")
            nombre=input("Ingrese el nombre del producto : ")
            valor=(int(input("Ingrese el valor del producto : ")))
            #aqui se crea una lista que ira a pasar a la lista principal
            #la penultima lista del codigo es donde vendra la info del proveedor o proveedores
            #la ultima lista sera donde viene la informacion de la venta 
            producto=[codigo.upper(),nombre.upper(),valor,[],[]]
            inventario.append(producto)
            rta=input("desea ingresar otro producto S o N : ")
            if rta.upper()=="S":
                isAddProduct=True
            elif rta.upper()=="N":
                isAddProduct=False
            else:
                print("respuesta no valida ")
                isAddProduct=True
    #aqui se buscara el id principal y despues se creara el penultimo y ultimo espacio de la lista anterior 
    elif option==2:
        palabra=input("Ingrese el codigo del producto a buscar : ")
        isAddProveedor=True
        prov=[]
        #se pueden ingresar 2 proveedores del mismo producto 
        for item in inventario:
            if palabra.upper() in item:
                while isAddProveedor==True:
                    idprov=input("Ingrese Identificacion del proveedor : ")
                    nombre=input("Ingrese nombre del proveedor : ")
                    ciudad=input("Ingrese ciudad del proveedor : ")
                    prov.append([idprov, nombre, ciudad])
                    rta=input("desea ingresar otro proveedor S o N : ")
                    if rta.upper()=="S":
                        isAddProveedor=True
                    elif rta.upper()=="N":
                        isAddProveedor=False
                    else:
                        print("respuesta no valida ")
                        isAddProveedor=True
                #el item[3] hace referencia al 4 puesto de la lista de inventario la que se crea vacia
                #el item[3] de la lista se haya por ciclo y se identifica mas facil por el id
                #y el .extend hace posible que hallan mas de un proveedor del mismo producto 
                item[3].extend(prov)
                print(inventario)
    elif option==3:
        #aqui se llena el ultimo espacio de la lista con datos de compra
        palabra=input("Ingrese el codigo del producto a comprar : ")
        isAddBuy=True
        for item in inventario:
            if palabra.upper() in item:
                while isAddBuy==True:
                    Cantidad=input("Ingrese el numero de objetos que desea adquirir : ")
                    nombre=input("Ingrese nombre del comprador : ")
                    ciudad=input("Ingrese ciudad del comprador : ")
                    direccion=input("Ingrese la direccion del comprador : ")
                    telefono=input("Ingrese el telefono del comprador : ")
                    vent.append([Cantidad, nombre, ciudad, direccion, telefono])
                    rta=input("desea ingresar otro Producto para comprar S o N : ")
                    if rta.upper()=="S":
                        isAddBuy=True
                    elif rta.upper()=="N":
                        isAddBuy=False
                    else:
                        print("respuesta no valida ")
                        isAddBuy=True
                #el item[4] hace referencia al puesto 5 de la lista principal que se creo vacia
                #el .extend deja crear elementos nuevos para distintos compradores del mismo producto
                item[4].extend(vent)
                #aqui vacio la lista vent para que no se repita la info
                vent=[]
                print(inventario)
    elif option==4:
        #print unicamente los productos 
        for i in range(0, len(inventario)):
            print(f"Codigo : {inventario[i][0]} ")
            print(f"Nombre : {inventario[i][1]} ")
            print(f"valor : {inventario[i][2]} ")
    elif option==5:
        # fin del programa
        rta=input("desea salir S o N : ")
        if rta.upper()=="S":
            isActiveMenu=False
        elif rta.upper()=="N":
            isActiveMenu=True
        else:
            print("respuesta no valida ")
            isActiveMenu=True
