valor = int(input("Digite um valor inteiro: "))

cedulas = [100, 50, 20, 10, 5, 2, 1]

print("Valor lido:", valor)
for cedula in cedulas:
    quantidade_notas = valor // cedula
    valor %= cedula
    print(quantidade_notas, "nota(s) de", cedula)

