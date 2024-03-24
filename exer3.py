valor = float(input("Digite um valor: "))

if valor >= 0 and valor <= 25:
    print("o valor esta no intervalo de [0,25]")
elif valor > 25 and valor <= 50:
    print("o valor esta no intervalo de (25,50]")
elif valor > 50 and valor <= 75:
    print("o valor esta no intervalo de (50,75]")
elif valor > 75 and valor <= 100:
    print("o valor esta no intervalo de (75,100]")
else:
    print("Fora de intervalo")
