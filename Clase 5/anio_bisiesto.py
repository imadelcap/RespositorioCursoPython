def anio_bisiesto(anio):

    #anio=int(input("Ingrese el año: "))

    if type(anio) != int:
        print("El dato ingresado no es válido")
        return None
    
    if anio % 400 == 0 or anio % 4 == 0 and anio % 100 !=0:
        print(f"El año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")
    

anio_bisiesto(100)
anio_bisiesto(400)
anio_bisiesto(1000)
anio_bisiesto(2012)
anio_bisiesto(1900)