from datetime import datetime, timedelta
print('{:=^40}'.format('Desafio 5'))
print('Marlon Lúcio ')
print('Prof : Cloves Rocha')
print('29/05/2026')
print('{:=^40}'.format('Datas'))


data_atual = datetime.now()

data_amanha = data_atual + timedelta(days=+1)

data_depois_de_amanha = data_atual + timedelta(days=+2)


print('Hoje :', data_atual.strftime("%d/%m/%Y"))
print(f'Depois de amanhã :{data_amanha.strftime('%d/%m/%Y')}')
print(
    f'Depois depois de amanhã : {data_depois_de_amanha.strftime('%d/%m/%Y')}')
