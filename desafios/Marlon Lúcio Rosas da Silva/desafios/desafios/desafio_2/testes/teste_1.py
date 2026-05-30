nome = input(
    'Olá, bem-vindo ao meu primeiro desafio em Python, por favor informe seu nome! ')

a = float(input('Certo {}, digite um número...'.format(nome)))
b = float(input('Agora digite outro número...'))
op = input('Qual operador ? (*, / , + , - , )')

if op == '+':
    resultado = a + b

elif op == '-':
    resultado = a - b

elif op == '*':
    resultado = a * b

elif op == '/':
    if b != 0:
        resultado = a / b
    else:
        resultado = None
        print('Erro : Divisão por 0')
if resultado is not None:
    print(f'O resultado é = {resultado}')
