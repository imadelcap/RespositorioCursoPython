print("Elija la opcion 1, 2 , 3 o 4.")
print("1. Soy un string - 4")
print("2. 4/0")
print("3. prnt('Mostrando Codigo'")
print("4. int('Quiero ser un Numero")

opcion = input("Que numero de opcion desea seleccionar:   ")

if opcion == "1" or "2" or "3" or "4":
    if opcion == "1":
        try:
            "string"-4
        except Exception as e:
            print(type(e).__name__)
    if opcion == "2":  
        print(type(1).__name__)
    if opcion == "3":
        print(TypeError)
    if opcion == "4":
        print(type(1).__name__)


