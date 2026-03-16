# Uninassau Paulista
# Docente: Cloves Rocha
# Estudante: Viviane Vitória
# Matrícula: 01750126
# Disciplina: Lógica de Programação

def processar_estatisticas():
    idades = []
    
    print("--- Cadastro de Idades ---")
    
    while len(idades) < 5:
        entrada = input(f"Digite a {len(idades) + 1}ª idade: ")
        
        # Verifica se a entrada é composta apenas por números inteiros ou outros caracteres
        if entrada.isdigit():
            valor = int(entrada)
            if valor > 0:
                idades.append(valor)  # .append adiciona os valores inteiros à lista

            else:
                print("Idade inválida! Digite um valor maior que 0.")
        else:
            print("Entrada inválida! Digite apenas números inteiros.")

    # Loop para idades extras se o usuário quiser
    while True:
        continuar = input("Deseja adicionar mais uma idade? (sim/nao): ")
        
        if continuar == 'nao':
            break
        elif continuar == 'sim':
            entrada = input(f"Digite a {len(idades) + 1}ª idade: ")
            
            if entrada.isdigit():
                valor = int(entrada)
                if valor > 0:
                    idades.append(valor)
                else:
                    print("Idade inválida!")
            else:
                print("Entrada inválida!")
        else:
            print("Responda apenas com 'sim' ou 'nao'.")

    maior = max(idades)
    menor = min(idades)
    media = sum(idades) / len(idades)
    contagem_maiores = sum(1 for idade in idades if idade >= 18)

    print("\n" + "="*30)
    print(f"MAIOR IDADE:        {maior} anos")
    print(f"MENOR IDADE:        {menor} anos")
    print(f"MÉDIA DE IDADES:    {media:.2f} anos")
    print(f"MAIORES DE 18 ANOS: {contagem_maiores} pessoas")
    print("="*30)

processar_estatisticas()