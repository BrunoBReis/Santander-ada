# Estrutura do for 

for variavel in range(10):
    # Começa a contar do 0 e repetiu 10 vezes
    print(variavel)

print("-----------------")

for variavel in range(1,10):
    # Começa do 1 e repetiu 9 vezes
    print(variavel)

print("-----------------")

for variavel in range(1,10,2):
    # Começa do 1 e vai de 2 em 2 até o 9
    print(variavel)

soma = 0
qtd_notas = 3

for i in range(1,qtd_notas + 1):
    nota = float(input(f"Qual a sua nota {i}"))
    soma = soma + nota

print("Media das notas ", soma / qtd_notas)