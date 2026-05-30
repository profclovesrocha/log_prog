
print('{:=^40}'.format('Bem-vindo'))
print('Marlon Lúcio ')
print('29/05/2026')
print('{:=^40}'.format('Calculadora'))
print('Bem-vindo, teste minha calculadora em Python.')
name = str(input('Por favor digite seu nome. '))


print('{:=^40}'.format('Lista de Operadores'))
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
op = input(f'Qual será a operação {name} ? ')
n1 = int(input('Certo por favor digite o primeiro número. '))

n2 = int(input(f'Agora digite outro número para continuar. '))

if op == '1':
    res = n1 + n2
elif op == '2' : 
    res = n1 - n2
elif op == '3' :
    res = n1 * n2
elif op == '4' :
    if n2 != 0 :
        res = n1 / n2
    else:
        res = None
       
    
print('{:=^40}'.format('Resultado'))

if res is not None :
    print(f'resulto foi {res}')
else:

    print('Não é possível dividir por 0')

