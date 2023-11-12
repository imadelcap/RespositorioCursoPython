num1= int(input('Ingrese primer numero: '))
num2= int(input('Ingrese segundo numero: '))

while True:
    
    opcion = input('Ingrese operacion \n 1. Suma \n 2. Resta \n 3. Multiplicacion \n 4. Finalizar \n Opcion: ')
    operacion = int(opcion)

    if operacion == 1:
        print('Resultado = ', num1 + num2)
    elif operacion == 2:
        print('Resultado = ', num1 - num2)
    elif operacion == 3:
        print('Resultado = ', num1 * num2)
    elif operacion == 4:
        break
    else:
        print('Opcion no valida')
        continue

    num1= int(input('Ingrese primer numero: '))
    num2= int(input('Ingrese segundo numero: '))
