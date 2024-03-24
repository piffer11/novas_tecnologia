maior_valor = None
posicao = None

for i in range(1, 101):
    valor = int(input(f"Digite o {i}º valor inteiro: "))
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor
        posicao = i

print("O maior valor lido é:", maior_valor)
print("Ele foi lido na posição:", posicao)
