p1 = float(input("Digite o preço do produto 1: "))
p2 = float(input("Digite o preço do produto 2: "))
p3 = float(input("Digite o preço do produto 3: "))
if p1 < p2 and p1 < p3:
    print(f"O produto com o menor preco é o 1, custando R${p1:.2f}")
elif p2 < p1 and p2 < p3:
    print(f"O produto com o menor preco é o 2, custando R${p2:.2f}")
else:
    print(f"O produto com o menor preco é o 3, custando R${p3:.2f}")