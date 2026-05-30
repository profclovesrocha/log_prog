print('{:=^40}'.format('Aluno'))
print('')
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('28/05/2026')
print('')
print('{:=^40}'.format('teste_02'))

print('')

print('{: ^40}'.format('Bem-vindo'))

print('')

nome = str(input('Por gentileza, poderia informar seu nome ? '))
idade = int(input(f'Obrigado {nome} ! Qual a sua idade ? '))

habilitacao = True
pode_dirigir = (idade >= 18 ) and (habilitacao == True)
print(f'Certo {nome}, confira se você tem permissão ou não. ')

print('')

print('{: ^40}'.format('Pode dirigir - True'))
print('{: ^40}'.format('Não Pode dirigir - False'))

print('')

print('{:=^40}'.format('Resultado'))

print('')

print(f'Resultado de {nome} : {pode_dirigir}')
print('')
