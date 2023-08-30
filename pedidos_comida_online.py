def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
        
    cupom = input()
    
    if "%" not in cupom:
        cupom += "%"
    
    desconto = 0.0
    
    if cupom == "10%":
        desconto = total * 0.1
    elif cupom == "20%":
        desconto = total * 0.2
    
    total_com_desconto = total - desconto
    
    print(f"Total dos pedidos: R$ {total:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_com_desconto:.2f}")
 
if __name__ == "__main__":
    main()
