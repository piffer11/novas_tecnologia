funcionario = int(input('Digite o número do funcionário: '))
horas = int(input('Digite o total de horas trabalhadas: '))
salario_hora = float(input('Digite seu salário por hora: '))

total_receber = horas * salario_hora

print(f"""NUMBER = {funcionario}
SALARY = U$ {total_receber}""")
