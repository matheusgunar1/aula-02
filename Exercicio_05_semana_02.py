"""
Exercício 05
Aluno: Matheus Gunar Ramalho Gomes
Data: 08/09/2022
"""
#Entrada de dados.
totalm = int(input("Digite o número total de mercadorias presentes no estoque: "))
i = 1 # É o contador.
soma = 0 # acumulador
#Procesamento de dados.
while i <= totalm:
    m1=float(input("Digite o valor da unidade de mercadoria: "))
    soma = soma + m1 # É o acumulador.
    i+=1
precomedio = soma/totalm
#Saída de dados.
print(f"Existem {totalm} mercadorias no estoque. O valor total em mercadorias é de R$ {soma} e o preço médio é de R$ {precomedio}.")

