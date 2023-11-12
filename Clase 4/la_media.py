count_num = int(input('Cuantos numeros quiere introducir?: '))

suma= 0
numeros = []

for i in range(count_num):
    numeros.append(int(input('Ingrese numero {}: '.format(i+1))))
    #sum =+ numeros[i]

suma = sum(numeros)
print('El promedio es', suma/count_num)