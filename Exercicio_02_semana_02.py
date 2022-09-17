"""
Exercício 02
Aluno: Matheus Gunar Ramalho Gomes
Data: 08/09/2022
"""
# Entrada de dados.

codigo = int(input("Digite seu código numérico: "))
anon = int(input("Digite seu ano de nascimento: "))
anot = int(input("Digite o ano em que você engressou na empresa: "))

#Processamento de dados e funções.

idade = 2022 - anon
tempot = 2022 - anot

#Saída de dados.

if idade >= 65 or tempot >= 30:
    print(f"O empregado código {codigo} de {idade} anos de idade com {tempot} anos de trabalho pode requerer aposentadoria.")
elif idade >= 60 and tempot >= 25:
    print(f"O empregado código {codigo} de {idade} anos de idade com {tempot} anos de trabalho pode requerer aposentadoria.")
else:
    print(f"O empregado código {codigo} de {idade} anos de idade com {tempot} anos de trabalho não requerer aposentadoria.")
