valor_hamburguer =  float(input())
quantidade_hamburguer =  float(input())
valor_bebida =  float(input())
quantidade_bebida =  float(input())
valor_pago =  float(input())

total_hamburguer = valor_hamburguer * quantidade_hamburguer
total_bebida = valor_bebida * quantidade_bebida
total_pedido = total_hamburguer + total_bebida

if valor_pago < total_pedido:
    while valor_pago < total_pedido:
        valor_pago = float(input())
    Troco = valor_pago - total_pedido
else:
    Troco = valor_pago - total_pedido if valor_pago > total_pedido else 0

print(f"O preço final do pedido é R$ {total_pedido:.2f}. Seu troco é R$ {Troco:.2f}.")