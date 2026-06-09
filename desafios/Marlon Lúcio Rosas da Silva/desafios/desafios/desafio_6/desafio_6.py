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
    
print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Dicionários'))

nome = input('Digite seu nome. ')
dicionario_1 = {
    'm1': {
        'm2':print(f'Olá {nome}')
    }
}


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

n = int(input('Digite um número inteiro : '))

res = verificar_impar_par(n)

print(f'O numero digitado foi {n}, e ele é {res}.')

print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print(' ')
print('{:=^40}'.format('Listas'))

notas = []

for n in range(4):
    nota = float(input(f'Digite sua {n+1}ª nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Nota máxima: {max(notas)}')
print(f'Nota mínima: {min(notas):.2f}')
print(f'Média: {media:.2f}')

notas = []

for n in range(4):
    nota = float(input(f'Digite sua {n + 1}ª nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)

if media >= 7:
    print(f'Sua média foi: {media} APROVADOOOO!!!!')
else:
    print(f'Infelizmente sua média foi: {media} Você foi para a final...')
    final = float(input('Digite a nota da prova final. '))
    nota_final = (media + final) /2
    if nota_final >= 7:
        print('Aprovado!')
    else:
        print('Você foi reprovado...')

print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Mensagens'))

print('Hello Wolrd')
print('')
nome_mensagem = input('Digite seu nome: ')
print(f'Muito obrigado {nome_mensagem}! Agora posso dar continuidade.')

print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Números'))
print(' ')

numero = int(input('Digite um número inteiro: '))

print('O número digitado foi: {}'.format(numero))
print('O sucessor desse número é: {}'.format(numero + 1))
print('O antecessor desse número é: {}'.format(numero - 1))

print('')

numero_int_float = float(input('Digite um número inteiro...'))
print(f'O número informado foi: {numero_int_float:.2f}')

print('')


print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Números'))
print(' ')

notas_2 = []

for n2 in range(4):
    nota_2 = float(input(f'Digite a nota da {n2 + 1}ª prova:'))
    notas_2.append(nota_2)
media_n2 = sum(notas_2) / len(notas_2)
print(f'Nota máxima: {max(notas_2):.2f}')
print(f'Nota mínima: {min(notas_2):.2f}')
print(f'Média: {media_n2}')

print('{:=^40}'.format('Aluno'))
print('Marlon Lúcio Rosas da Silva')  
print('Professor : Cloves Rocha')
print('Turma : ADS')
print('03/06/2026')
print('{:=^40}'.format('Números'))
print(' ')

print('{:=^40}'.format(' PAR OU ÍMPAR '))

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é ÍMPAR.')


frase = 'Exercícios de Java'

nova_frase = frase.replace('Java', 'Python')

print(nova_frase)

print('{:=^40}'.format(' PRIMEIRO E ÚLTIMO NOME '))

nome_completo = input('Digite seu nome completo: ').strip()

nomes = nome_completo.split()

print(f'Primeiro nome: {nomes[0]}')
print(f'Último nome: {nomes[-1]}')

print('{:=^40}'.format(' PAR OU ÍMPAR '))

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é ÍMPAR.')

    print('{:=^40}'.format(' CALCULADORA '))

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

print('\nEscolha a operação:')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opcao = int(input('Opção: '))

if opcao == 1:
    resultado = n1 + n2
    print(f'Resultado: {n1} + {n2} = {resultado}')

elif opcao == 2:
    resultado = n1 - n2
    print(f'Resultado: {n1} - {n2} = {resultado}')

elif opcao == 3:
    resultado = n1 * n2
    print(f'Resultado: {n1} × {n2} = {resultado}')

elif opcao == 4:
    if n2 != 0:
        resultado = n1 / n2
        print(f'Resultado: {n1} ÷ {n2} = {resultado}')
    else:
        print('Erro: divisão por zero!')

else:
    print('Opção inválida!')

    print('{:=^40}'.format(' CELSIUS PARA FAHRENHEIT '))

temperaturas_c = [22.5, 40, 13, 29, 34]

temperaturas_f = []

for celsius in temperaturas_c:
    fahrenheit = (celsius * 9/5) + 32
    temperaturas_f.append(fahrenheit)

print('Temperaturas em Celsius:', temperaturas_c)
print('Temperaturas em Fahrenheit:', temperaturas_f)

print('{:=^40}'.format(' SOMA DE PARES E ÍMPARES '))

numeros = [21, 5, 34, 8, 16, 7, 3]

soma_pares = 0
soma_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f'Soma dos pares: {soma_pares}')
print(f'Soma dos ímpares: {soma_impares}')

print('{:=^40}'.format(' MAIOR E MENOR VALOR '))

numeros = [54, 10, 29, 87, 7, 64]

maior = max(numeros)
menor = min(numeros)

print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')






    






    

