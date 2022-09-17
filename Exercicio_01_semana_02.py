"""
Exercício 01
Aluno: Matheus Gunar Ramalho Gomes
Data:08/09/2022
"""
# Entrada de dados.
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua seguda nota: "))
n3 = float(input("Digite sua terceira nota: "))
# Processamento de dados e funções.
media = (n1+n2+n3)/3

if media >= 9.0:
    print(f"Seu conceito foi A com média igual a {media}.")
else:
    if media >= 7.5 and media < 9:
        print(f"Seu conceito foi B com média igual a {media}.")
    elif media >= 6.0 and media < 7.5:
        print(f"Seu conceito foi C com média igual a {media}.")
    else:
        print(f"Seu conceito foi D com média igual a {media}.")

