# PROFESSOR: CLOVES ROCHA 
# ALUNO: JOÃO APULO ROMÃO SAMPAIO DE MELO 
# MATRICULA: 01871330
# DISCIPLINA: LOGICA DA PROGRAMAÇÃO





from datetime import date, timedelta

hoje = date.today()
dois_dias_depois = hoje + timedelta(days=2)



print(f"hoje: {hoje}")
print(f"Daqui 2 dias: {dois_dias_depois}")

print(hoje.strftime("%d/%m/%y"))
print(dois_dias_depois.strftime("%d/%m/%y"))


# DICIANARIO

Dados = {"m1" : {"m2" : "olá mundo"}}
                 
mensagem = Dados["m1"]["m2"]
print(mensagem)

# FUNÇÕES

def verificar_PAR_IMPAR(numero):
    if numero % 2==0:
        return f"{numero} é PAR"
    else:
        return f"{numero} é IMPAR"
    

print(verificar_PAR_IMPAR(4))
print(verificar_PAR_IMPAR(5))

# NOTAS

notas = [8, 7, 9.5, 7, 5]
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f"media final: {media:.1f}")
print(f"maior nota: {maior}")
print(f"menor nota: {menor}")

notas = [8, 7, 9.5, 7, 5]
media = sum(notas) / len(notas)

print(f"media final: {media:.1f}")

if media >= 7:
    print("APROVADO")
else:
    nota_final = 7.3
    nova_media = (media + nota_final) / 2
    print(f"nova media:{nova_media:.1f}")
    if nova_media >= 7:
        print("APROVADO")
    else:
        print("REPROVADO")


# MENSAGENS

print("Hello World")

nome = input("Qual o seu nome? ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")

# NUMEROS 

numero = int(input("digite um numero"))
print(f"Antecessor: {numero - 1}")
print(f"numero: {numero}")
print(f"sucessor: {numero + 1}")

numero = float(input("digite umn numero"))
print(f"{numero:.2f}")

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

media = (n1 + n2 + n3 + n4) / 4
print(f"media final: {media:.2f}")

numero = int(input("Digite um numero"))

numero = float(input("Digite um numero"))
resultado = "PAR" if numero % 2 == 0 else "IMPAR"
print(f"{numero} é {resultado}")


op = input("Operação (+, -, *, /): ")
a = float(input("Valor 1: "))
b = float(input("Valor 2: "))

if op == "+": resultado = a + b
elif op == "-": resultado = a - b
elif op == "*": resultado = a * b
elif op == "/" and b != 0:
    resultado = a / b
else:
    print("Operação inválida ou divisão por zero")
    resultado = None

    if resultado is not None:
        print(f"Resultado:{resultado:.2f}")

# MAPA

if numero % 2 == 0:
    print(f"{numero} é PAR")
else: 
    print(f"{numero} é IMPAR")


# STRING

frase= "Exercicios de Java"
nova_frase = frase.replace("java", "Python")
print(nova_frase)
 
# AVANÇADO


nome_completo = input("Nome completo: ")
partes = nome_completo.split()

primeiro = partes[0]
ultimo = partes[-1]
print(f"{primeiro} {ultimo}")



celsius = [22.5, 40, 13, 29, 34]

fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

for c, f in zip(celsius, fahrenheit):
    print(f"{c}°c -> {f:.1f}°f")

seq = [21, 5, 34, 8, 16, 7, 3]

pares = list(filter(lambda x: x % 2 == 0, seq))
impares = list(filter(lambda x: x % 2 != 0, seq))


print(f"Pares: {pares} -> soma = {sum(pares)}")
print(f"Impares: {impares} -> soma = {sum(impares)}")

seq = [54, 10, 29, 87, 7, 64]

print(f"Sequencia: {seq}")
print(f"Maior: {max(seq)}")
print(f"Menor: {min(seq)}")