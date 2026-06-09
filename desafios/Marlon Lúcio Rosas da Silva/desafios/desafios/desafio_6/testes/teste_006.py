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