nomeRestaurante = input("Digite o nome do restaurante: ")

while True:
    try:
        tempoEstimadoEntrega = int(input("Digite o tempo estimado de entrega em minutos: "))
        break
    except ValueError:
        print("Digite um valor numérico válido para o tempo estimado de entrega.")

print(f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")
