# 02/06/2026 #
print('{:=^60}'.format('Calculadora'))
print('{: ^60}'.format('Operadores'))

print('(/) - Divisão')
print('(x) - Multiplicação')
print('(+) - Adição')
print('(-) - Subtração')

n1 = int(input('Primeiro número'))

op = input('Operação')

n2 = int(input('Segundo número'))

if op == '+' :
    res = n1 + n2
elif op == '-' :
    res = n1 - n2
elif op == 'x':
    res = n1 * n2
elif op == '/':
    if n2 != 0:
        res = n1 / n2
    else:
        res = None 
        print ('Erro')

if res is not None :
    print ('res')
