nome = str(input('Digite seu nome: '))
salario_fixo = float(input('Digite o valor do seu salário fixo: '))
total_vendas = float(input('Digite o total de vendas efetuadas: '))

total_receber = (total_vendas * 0.15) + salario_fixo

print(f'TOTAL = R${total_receber:.2f}')