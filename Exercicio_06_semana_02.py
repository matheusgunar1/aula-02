"""
Exercício 06
Aluno: Matheus Gunar Ramalho Gomes
Data: 09/09/2022
"""
#Entrada de dados.
soma = 0 # acumulador.
i = 0  # É o contador.
resp = "s"
while resp == "s":
    m1=float(input("Digite o valor da unidade de mercadoria: "))
    soma = soma + m1 # É o acumulador.
    i+=1
    resp = input("Deseja inserir mais mercadorias (S/N)? ")
precomedio = soma/i
#Saída de dados.
print(f"Existem {i} mercadorias no estoque. O valor total em mercadorias é de R$ {soma} e o preço médio é de R$ {precomedio}.")

