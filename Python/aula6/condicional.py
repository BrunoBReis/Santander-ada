# Estrutura condicional 

"""
Imagine que você queria imprimir "Aprovada(o)", caso o estudante tenha uma
média superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7
"""

nota = float(input("Qual foi a sua nota dos exames\n"))

if ((nota >= 0) and (nota <= 10)):
    if (nota >= 7):
        print("Aprovada(o)")
    else:
        print("Reprovado")
else:
    print("Valor de nota inválido")
