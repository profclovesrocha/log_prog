
notas_2 = []

for n2 in range(4):
    nota_2 = float(input(f'Digite a nota da {n2 + 1}ª prova:'))
    notas_2.append(nota_2)
media_n2 = sum(notas_2) / len(notas_2)
print(f'Nota máxima: {max(notas_2):.2f}')
print(f'Nota mínima: {min(notas_2):.2f}')
print(f'Média: {media_n2}')
