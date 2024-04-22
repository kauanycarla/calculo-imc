def calcular_preco(chegada, partida):
    horas_chegada, minutos_chegada = chegada
    horas_partida, minutos_partida = partida

    minutos_total_chegada = horas_chegada * 60 + minutos_chegada
    minutos_total_partida = horas_partida * 60 + minutos_partida

    minutos_estacionado = minutos_total_partida - minutos_total_chegada
    horas_estacionado = -(-minutos_estacionado // 60)  # Arredonda para cima

    if horas_estacionado <= 2:
        preco = horas_estacionado * 1
    elif horas_estacionado <= 4:
        preco = 2 + (horas_estacionado - 2) * 1.4
    else:
        preco = 4.80 + (horas_estacionado - 4) * 2

    return preco

# Solicita ao usuário que insira os momentos de chegada e de partida
chegada = tuple(map(int, input("Digite a hora e os minutos de chegada (HH MM): ").split()))
partida = tuple(map(int, input("Digite a hora e os minutos de partida (HH MM): ").split()))

# Calcula o preço do estacionamento e exibe o resultado
preco = calcular_preco(chegada, partida)
print(f"O preço cobrado pelo estacionamento é R$ {preco:.2f}.")
