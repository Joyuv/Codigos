m = []
while True:
    car = []

    car.append(input('Insira o modelo do veículo: '))
    car.append(input('Insira a cor do veículo: '))
    car.append(input('Insira a placa do veículo: '))
    
    zezo = input('Deseja inserir mais veículos? (s/n): ')
    zezo = zezo.lower()
    
    m.append(car)

    if zezo == 's':
        pass
    if zezo == 'n':
        break

for x in range(0, len(m)):
    print(f'Modelo: {m[x][0]}, Cor: {m[x][1]}, Placa: {m[x][2]}')