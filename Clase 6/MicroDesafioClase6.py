def dividir(a, b):
    if b == 0:
        return None
    return a / b

print(dividir(1,0))
print(dividir(7,2))

def dividir_2(a, b):
    try:
        return a/b
    #except ZeroDivisionError:
    #return None
    
    except Exception as error:
        print("La operación no se pudo completar: ", error)

print(dividir_2(1,0))
print(dividir_2(7,2))
