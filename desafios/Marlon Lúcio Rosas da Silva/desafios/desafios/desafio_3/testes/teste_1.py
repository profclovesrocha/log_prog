print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('28/05/2026')

print('{:=^40}'.format('Teste'))

nome = str(input('Seja bem-vindo, qual seu nome ? '))

n1 = int(input(f'Certo {nome}, digite um número. '))

n2= int(input('Obrigado, agora digite outro número para que ocorra as relações. '))

print('{:=^40}'.format('Resultado'))

if n1 == n2 :
    resultado = print(f'O {n1} é igual a {n2} ou seja {n1} == {n2}')
elif n1 > n2 or n1 >= n2:
    resultado = print(f'O {n1} é maior que {n2} ou seja {n1} > {n2} e também dependendo do contexto {n1} >= {n2}')
elif n1 < n2 or n1 <= n2:
    resultado = print(f'O {n1} é menor que {n2} ou seja {n1} < {n2} e também também dependendo do contexto {n1} <= {n2}')
print('{:=^40}'.format('Teste finalzado'))
print(f'Obrigado pela participação {nome} !')