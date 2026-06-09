notas = []

for n in range(4):
    nota = float(input(f'Digite a {n + 1}ª nota: '))
    notas.append(nota)
media = sum(notas) / len(notas)

print(f'Sua nota máxima foi de: {max(notas):.2f}')
print(f'Sua menor nota foi de: {min(notas):.2f}')
print(f'Sua média foi de: {media}')
