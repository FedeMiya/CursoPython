#7) Ingresar las temperaturas registradas a distintas horas de un día en grados hasta que
#ésta sea 100. Mostrar la temperatura máxima y la temperatura mínima.
temperatures = [

]
while 100 not in temperatures:
    newTemperature = input('Ingrese un valor de temperatura: ')
    if newTemperature.isnumeric():
            temperatures.append(int(newTemperature))
print(f'La temperatura máxima fue de {max(temperatures)}')
print(f'La temperatura mínima fue de {min(temperatures)}')