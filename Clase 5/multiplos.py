def es_multiplo():

    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))

    if n1 % n2 == 0:
        resultado = 'El número {} es múltiplo de {}'.format(n1,n2)
    elif n2 % n1 == 0:
        resultado = 'El número {} es múltiplo de {}'.format(n2,n1)
    else:
        resultado = 'No son múltiplos'
    
    return resultado

print(es_multiplo())


    
    