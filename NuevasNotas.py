Alumno =[]
ListaAlumnos =[]
isActive = True 
Opcion = 0
while isActive==True:
    print("*******\tSIRN--UNAB\t*******")
    print("1. Registrar Alumno\n2. Buscar Alumno\n3. Ingresar Calificaciones\n4. Listar Alumnos\n"+
    "5. Dar de baja\n6. Salir")
    Opcion=int(input())
    if Opcion==1:
        print("*** Registro de Alumnos ***")
        isAddStudent=True
        while isAddStudent == True:
            codigo = input("Ingrese el Codigo del Alumno : ")
            nombre = input("Ingrese el nombre del Alumno : ")
            Alumno =[codigo,nombre,[]]
            ListaAlumnos.append(Alumno)
            isAddStudent=bool(input("Si desea ingresar otro Alumno Presione S\nde lo contrario Presione Enter"))
    elif Opcion==2:
            print("*** buscador de Alumnos***")
            isAddNot= True
            while isAddNot==True:
                palabra=input("escriba el codigo del estudiante : ")
                for i in range(0, len(ListaAlumnos)):
                    if palabra in ListaAlumnos[i]:
                        print(f"Codigo : {ListaAlumnos[i][0]} ")
                        print(f"Nombre : {ListaAlumnos[i][1]} ")
                        print(f"Notas : {ListaAlumnos[i][2]} ")
                        break
                    elif i==(len(ListaAlumnos)-1):
                        print("Alumno no pertenece al grupo")
                isAddNot=bool(input("Si desea Consultar otro Alumno Presione S\nde lo contrario Presione Enter"))       
    elif Opcion==3:
        print("*** Registro de Calificaciones***")
        notasParciales=[]
        notasQuices=[]
        notasTarea=[]
        
        isAddNot=True
        while isAddNot==True:
            palabra=input("escriba el codigo del estudiante : ")
            isNotaActiva=True
            for i in range(0, len(ListaAlumnos)):
                if palabra in ListaAlumnos[i]:
                    while isNotaActiva ==True:
                        #aqui estan las notas de los 3 parciales
                        Notaparcial1=float(input("ingrese la primera calificacion de parcial : "))
                        notasParciales.append(Notaparcial1)
                        Notaparcial2=float(input("ingrese la segunda calificacion de parcial : "))
                        notasParciales.append(Notaparcial2)
                        Notaparcial3=float(input("ingrese la tercera calificacion de parcial : "))
                        notasParciales.append(Notaparcial3)
                        print( notasParciales)
                        #aqui esta la nota final de los parciales
                        NotasParciales4= ((Notaparcial1+Notaparcial2+Notaparcial3)/3)*0.60
                        notasParciales.append(NotasParciales4)
                        print(f"esta es la nota final de los parciales que equivale al 60% de la nota {notasParciales[3]}")
                        #aqui estan las notas de los quices 
                        NotaQuiz1=float(input("ingrese la primera calificacion de quiz : "))
                        notasQuices.append(NotaQuiz1)
                        NotaQuiz2=float(input("ingrese la segunda calificacion de quiz : "))
                        notasQuices.append(NotaQuiz2)
                        NotaQuiz3=float(input("ingrese la tercera calificacion de quiz : "))
                        notasQuices.append(NotaQuiz3)
                        NotaQuiz4=float(input("ingrese la cuarta calificacion de quiz : "))
                        notasQuices.append(NotaQuiz4)
                        print(notasQuices)
                        #aqui esta la nota final de los quiz
                        NotaQuiz5 = ((NotaQuiz1 + NotaQuiz2 + NotaQuiz3 + NotaQuiz4)/4)*0.25
                        notasQuices.append(NotaQuiz5)
                        print(f" esta es la nota final de los quiz que equivale al 25% de la nota final {notasQuices[4]} ")
                        #aqui esta las notas de las tareas
                        NotaTarea1=float(input("ingrese la primera calificacion de la Tarea : "))
                        notasTarea.append(NotaTarea1)
                        NotaTarea2=float(input("ingrese la segunda calificacion de la Tarea : "))
                        notasTarea.append(NotaTarea2)
                        #aqui esta la nota final de las tareas
                        NotaTarea3 = ((NotaTarea1 + NotaTarea2)/2)*0.15
                        notasTarea.append(NotaTarea3)
                        print(f"esta es la nota final de las tareas que equivale al 15% de la nota final {notasTarea[2]} ")

                        NotaFinal= float(NotasParciales4 + NotaQuiz5 + NotaTarea3)
                        print(f"esta es la nota final del curso del estudiante {NotaFinal} ")

                        isNotaActiva=bool(input("Desea ingresar otra nota para el Alumno\n actual . "+
                        "S o Enter para No "))
                        #aqui es donde la nota final de los parciales,quizes y tareas se unen a la lista
                        ListaAlumnos[i][2].append(NotaFinal)
                        notasParciales=[]
                        notasQuices=[]
                        notastarea=[]
                        break
                elif i==(len(ListaAlumnos)-1):
                    print("El alumno no pertenece al grupo")
            isAddNot=bool(input("desea Ingresar notas a otro Alumno Presione S\nde lo contrario Presione Enter"))
    elif Opcion==4:
        print("*** Lista general de Alumnos ***")
        for i in range(0, len(ListaAlumnos)):
            print(f"Codigo : {ListaAlumnos[i][0]} ")
            print(f"Nombre : {ListaAlumnos[i][1]} ")
            print(f"Notas : {ListaAlumnos[i][2]} ")
    elif Opcion==5:
        print("*** Dar de baja a Alumno ***")
        isAddNot=True
        while isAddNot==True:
            palabra=input("escriba el codigo del estudiante ")
            for i in range(0, len(ListaAlumnos)):
                if palabra in ListaAlumnos[i]:
                    rta=input("Seguro S  otra opcion cancela")
                    if rta=="s" or rta=="S":
                        del ListaAlumnos[i]
                        #termina el ciclo
                        break
                    else:
                        print("cancelado")
                elif i==(len(ListaAlumnos)-1):
                    print("el alumno no pertence")
            isAddNot=bool(input("Desea dar de baja a otro estudiante S o Enter para No "))
                
    elif Opcion==6:
        print("*** gracias por usar nuestro servicio***")
        isActive==False
    else:
        print("**** Opcion no permitida***")



                    
            
