def dividir(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("La operación no se pudo completar porque hay una división por cero.")
    except TypeError:
        print("Hubo un error en los tipos de datos.")
    except NameError:
        print("El argumento apunta a una variable inexistente.")
    except Exception as error:
        print("No se pudo completar porque: ", error)


print(dividir(34,7))
print(dividir(34,0))
print(dividir(34,"String"))
print(dividir(34,(45,"asdf")))
#print(dividir(34, variabe_no_existente))