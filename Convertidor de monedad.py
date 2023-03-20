

EUR = 0.93
PER = 3.79
CHI = 823.21

Nombre = input('Cual es su nombre: ')

print(f"Hola {Nombre}, bienvenido al conversor de monedas")
print('Seleccione una de las siguientes opciones de conversión')

print("1 - Dolares estadounidense a Euros")
print("2 - Dolares estadounidense a soles Peruanos")
print("3 - Dolares estadounidense a pesos chilenos")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    dolares = int(input("Cuantos dolares tiene: "))
    Moneda = dolares * EUR
    print(f"tienes {Moneda} Euros")
else:
    if opcion == 2:
        dolares = int(input("Cuantos dolares tiene: "))
        Moneda = dolares * PER
        print (f"Tiens {Moneda} soles Peruanos")
    else:
        if opcion == 3:
            dolares = int(input("Cuantos dolares tienes: "))
            Moneda = dolares * CHI
            print(f"Tienes {Moneda} pesos Chilenos")
        
        
