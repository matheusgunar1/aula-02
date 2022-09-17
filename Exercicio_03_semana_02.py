"""
Exercício 03
Aluno: Matheus Gunar Ramalho Gomes
Data:08/09/2022
"""
# Entrada de dados.

a = float(input("Digite um número qualquer: "))
b = float(input("Digite um outro número qualquer diferente de zero: "))
c = 1

# Processamento de dados e funções.

if b == 0:
    b = c
    divisao = a/b
    print(f"O resultado da divisão de {a} por {b} foi de {divisao}. Erro não existe divisão por 0.")
else:
    divisao = a/b
    print(f"O resultado da divisão de {a} por {b} foi de {divisao}.")
