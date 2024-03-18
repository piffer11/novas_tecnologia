A = int(input('Digite o primeiro valor inteiro: '))
while A < 0 or A > 10:
    print("Nota abixo do valor permitido (0 a 10).")
    A = int(input('Digte o valor novamente: '))

B = int(input('Digite o segundo valor inteiro: '))
while B < 0 or B > 10:
    print("Nota abixo do valor permitido (0 a 10).")
    B = int(input('Digte o valor novamente: '))

C = int(input('IDigite o terceiro valor inteiro: '))
while C < 0 or C > 10:
    print("Nota abixo do valor permitido (0 a 10).")
    C = int(input('Digte o valor novamente: '))

MEDIA = ((A * 2) + (B * 3) + (C * 5)) / 10

print(f'MEDIA = {MEDIA:.1f}')