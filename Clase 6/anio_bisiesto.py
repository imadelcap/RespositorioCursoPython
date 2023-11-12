def anio_bisiesto():

    try:
        anio=int(input("Ingrese el año: "))

    except:
        print("No se ingresó un dato válido")
        anio_bisiesto()
        print("salio")
        return None

    
    if anio % 400 == 0 or anio % 4 == 0 and anio % 100 !=0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto()
