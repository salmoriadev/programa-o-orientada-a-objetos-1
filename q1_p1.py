codigo, quantidade = input().split()

match codigo:
    case "1":
        preco_unitario = 4
    case "2":
        preco_unitario = 4.5
    case "3":
        preco_unitario = 5
    case "4":
        preco_unitario = 2
    case "5":
        preco_unitario = 1.5
        
preco_final = preco_unitario * int(quantidade)
print(f"Total: R$ {preco_final:.2f}")