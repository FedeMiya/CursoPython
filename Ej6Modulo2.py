#) Leer dos números, mostrar el siguiente Menú pudiendo seleccionar alguna opción y
#repetir esta operación hasta que seleccione 5.
 #Menú principal
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
# Seleccione una opción:

numero_1 = int(input('Ingrese el primer número: '))
numero_2 = int(input('Ingrese el segundo número: '))
menu = {
  1: 'Sumar',2: 'Restar',3: 'Multiplicar',4: 'Dividir',5: 'Salir'
  }
menuTrack = 0

while menuTrack != 1:
  print(menu)
  seleccionMenu = int(input('Seleccione una opción: '))
  if seleccionMenu == 1:
    print(numero_1+numero_2)
  elif seleccionMenu == 2:
    print(numero_1-numero_2)
  elif seleccionMenu == 3:
    print(numero_1*numero_2)
  elif seleccionMenu == 4:
    print(numero_1/numero_2)
  elif seleccionMenu == 5:
    menuTrack += 1
  else:
    print('Ingresaste un número inválido')