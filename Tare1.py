# Calcular el promedio de una cantidad de N cantidad de numeros enteros

Nombre = input('Cual es su nombre: ')
print(f"Hola {Nombre}, bienvenido, revise su promedio de calificaciones")

Nota1 = float(input("Ingrese calificación 1: "))
Nota2 = float(input("Ingrese calificación 2: "))
Nota3 = float(input("Ingrese calificación 3: "))

#Operacion
Promedio = (Nota1 + Nota2 + Nota3) / 3
# Condición
if Promedio >=7:
    print("Aprobado")
else:
    print("Reprobado")     
    
    