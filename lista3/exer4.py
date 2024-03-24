# Ler os 3 valores inteiros em entradas separadas
num1 = int(input("Digite o primeiro valor inteiro: "))
num2 = int(input("Digite o segundo valor inteiro: "))
num3 = int(input("Digite o terceiro valor inteiro: "))

numeros = [num1, num2, num3]

numeros_ordem_crescente = sorted(numeros)

print("Valores em ordem crescente:", *numeros_ordem_crescente)

print("Valores na sequência em que foram lidos:", num1, num2, num3)
