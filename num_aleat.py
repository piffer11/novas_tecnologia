import random

numero_secreto = random.randrange(0, 101)  
tentativas_totais = 10

for tentativa_atual in range(1, tentativas_totais + 1):
    chute = int(input("Digite um número entre 0 e 100: "))
    tentativas_restantes = tentativas_totais - tentativa_atual

    if chute > numero_secreto:
        print("Seu chute foi maior que o número secreto. Tentativas restantes:", tentativas_restantes)
    elif chute < numero_secreto:
        print("Seu chute foi menor que o número secreto. Tentativas restantes:", tentativas_restantes)
    else:
        print("Parabéns! Você acertou o número secreto.")
        break

if tentativa_atual == tentativas_totais and chute != numero_secreto:
    print("Você usou todas as tentativas. O número secreto era:", numero_secreto)
