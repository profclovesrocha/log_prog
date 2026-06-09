notas = []

for n in range(4):
    nota = float(input(f'Digite a {n + 1}° nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Sua nota média: {media:.2f}')
print(f'Sua nota máxima: {max(notas):.2f}')
print(f'Sua nota mínima: {min(notas):.2f}')







