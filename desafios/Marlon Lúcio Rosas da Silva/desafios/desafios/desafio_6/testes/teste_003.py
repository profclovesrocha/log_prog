print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Funções'))

def verificar_impar_par(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'

n = int(input('Digite um númeor inteiro : '))

res = verificar_impar_par(n)

print(f'O numero digitado foi {n}, e ele é {res}')

