def main():
    numPedidos = int(input())
    pedidos = []

    for i in range(1, numPedidos + 1):
        prato = input()
        calorias = int(input())
        ehVegano = input() == "s"

        pedidos.append((prato, calorias, ehVegano))

    for i, pedido in enumerate(pedidos, start=1):
        prato, calorias, ehVegano = pedido
        tipoVegano = "Vegano" if ehVegano else "Nao-vegano"
        print(f"Pedido {i}: {prato} ({tipoVegano}) - {calorias} calorias")
    
if __name__ == "__main__":
    main()