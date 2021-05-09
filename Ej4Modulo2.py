#4) Leer el número de mes y mostrar cuantos días tiene ese mes (año actual)

mes = int(input('Ingrese el número de mes: '))

if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
   print('El mes ingresado tiene 31 días')
elif mes == 4 or 6 or 9 or 11:
    print('El mes ingresado tiene 30 días')
elif mes == 2:
    print('El mes ingresado tiene 28 días')
else:
    print('El mes ingresado es inválido')