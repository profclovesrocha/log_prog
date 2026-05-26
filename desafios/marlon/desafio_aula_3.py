# Desafio 1 — Construindo uma calculadora simples em Python

nome = input('Olá, bem-vindo ao meu primeiro desafio em Python, por favor informe seu nome: ')

n1 = int(input(f'Obrigado {nome}! Agora digite um número: '))
n2 = int(input('Agora digite outro: '))

print('Escolha a operação')
print(' 1 - Multiplicação')
print(' 2 - Divisão')
print(' 3 - Adição')
print(' 4 - Subtração')

op = input(f'Qual operador você escolheu, {nome}? ')

if op == '1':
    resultado = n1 * n2
elif op == '2':
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = None
        print('Erro : Divisão por 0')
elif op == '3':
    resultado = n1 + n2
elif op == '4':
    resultado = n1 - n2

else:
    resultado = None
    print('Operação inválida...')

if resultado is not None:
    print(f'O resultado foi {resultado}')




