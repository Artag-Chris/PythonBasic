i= 1
AproveStudents = 0
ReproveStudents = 0
AproveStudentsNames =[]
ReproveStudentsNames= []
#AproveStudentsNotes =[]
#ReproveStudentsNotes =[]
#FullAproveInfo = [[AproveStudentsNames], [AproveStudentsNotes]]
#FullReproveInfo = [[ReproveStudentsNames], [ReproveStudentsNotes]]
StudentsToGrade = int(input("Cuantos estudiantes vas a calificar? "))
"""
estudiar matrices
buscar como crear variables con el return 
"""

def Note1  (array):
    sum = 0
    for element in array:
        sum += element / 3
    return sum
def Note2  (array):
    sum2 = 0
    for element in array:
        sum2 += element / 4 
    return sum2
def Note3  (array):
    sum3 = 0
    for element in array:
        sum3 += element / 2
    return sum3
while i <= StudentsToGrade:
    StudentName = input("Cual es el nombre del estudiante?  ")
    a = float(input("ingrese la nota del primer parcial  "))
    b = float(input("ingrese la nota del segundo parcial  "))
    c = float(input("ingrese la nota del tercer parcial  "))
    partials=[a,b,c]
    print(partials)
    print(f" Esta es la nota final de los parciales  {Note1(partials)}")
    PartialPorcentage= ((a + b + c)/3)*0.6
    print(f" Esta nota equivale al 60% total de la materia {PartialPorcentage}")
    d = float(input("ingrese la primera nota del quiz  "))
    e = float(input("ingrese segunda nota del quiz  "))
    f = float(input("ingrese tercera nota del quiz  "))
    g = float(input("ingrese nota del quiz final   "))
    quices = [d,e,f,g]
    print(quices)
    print(f" esta es la nota por los quiz {Note2(quices)}")
    QuizesPorcantage= ((d + e + f + g)/4)*0.25
    print(f" esta nota equivale al 25% total de la nota y es {QuizesPorcantage}")
    h = float(input("ingrese nota de la primera tarea  "))
    j = float(input("ingrese nota de la ultima tarea  "))
    Homework = [h,j]
    print(Homework)
    print(f" esta es la nota final de las tareas  {Note3(Homework)}")
    HomeworkPorcentage= ((h + j)/2)*0.15
    print(f" esta nota equivale al 15% total de la nota {HomeworkPorcentage}")
    FinalNote = PartialPorcentage + QuizesPorcantage + HomeworkPorcentage
    print(FinalNote)
    if FinalNote >= 3.5:
        print(f"el estudiante {StudentName} aprobo con {FinalNote} felicitaciones!!!!!!")
        i +=1
        AproveStudents += 1
        Student =[]
        Student.append(f"{StudentName} ")
        Student.append(FinalNote)
        AproveStudentsNames.append(Student)
        
        
       # print(AproveStudentsNames)
    else:
        print(f"el estudiante {StudentName} perdio con {FinalNote} de seguro le dan rejo")
        i +=1
        ReproveStudents +=1
        Student =[]
        Student.append(f"{StudentName} ")
        Student.append(FinalNote)
        ReproveStudentsNames.append(Student)
        

       #print(ReproveStudentsNames)
"""
buscar como decir que un array no tiene nada
if ReproveStudentsNames[0]:
    ReproveStudentsNames.append("ninguno")
elif AproveStudentsNames[0]:
    AproveStudentsNames.append("ninguno")
"""

    
print(f"el numero de estudiantes aprobados es {len(AproveStudentsNames)} son {AproveStudentsNames}  \n y de los reprobados es {ReproveStudents} y son {ReproveStudentsNames}")

"""
def PrintMatriz(FullAproveInfo):
    for i in range(len(FullAproveInfo)):
      for j in range(len(FullAproveInfo[i])):
        print(FullAproveInfo[i][j], end=" ")
    print()
"""
Txt = open("clase 1.txt", "w")
"""
for i in AproveStudentsNames:
for i in ReproveStudentsNames:
    """
Txt.write(f" estos son los estudiantes aprobados {AproveStudentsNames}  \n")

Txt.close()
Txt = open("clase 1.txt", "a")
Txt.write(f" estos son los reprobados: {ReproveStudents}")
Txt.close()
print("gracias por el tiempo ty")
