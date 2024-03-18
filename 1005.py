A = float(input('Digite a primeira nota: '))
while A < 0 or A > 10:
    print("Nota abaixo do valor permitido (0 a 10).")
    A = float(input('Digite a nota novamente: '))

B = float(input('Digite a segunda nota: '))
while B < 0 or B > 10:
    print("Nota abaixo do valor permitido (0 a 10).")
    B = float(input('Digite a nota novamente: '))

A = A * 3.5
B = B * 7.5
media = (A + B) / (3.5 + 7.5)

print(f'MEDIA = {media:.4f}')
