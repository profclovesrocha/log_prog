print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Datas'))
from datetime import datetime, timedelta

print('Escolha umas dessas opções.')
print('1 - Data de Hoje.')
print('2 - Data depois de amanhã.')
data_atual = datetime.now().date()
data_futura = data_atual + timedelta(days=2)
op = input('')

if op == '1':
    res = print(data_atual)

elif op == '2':
    res = print(data_futura)

elif (op == '0') or (op > '2'):
    res = print('Opção inválida...')
    

    




    

