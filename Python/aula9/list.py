# Lista

# Neste caso eu consigo armazenar varias informações dentro de uma variável 

notas = [7.5, 8.75, 9, 10, 4.4]

lista = list() # Cria-se a uma lista vazia
lista1 = [1, 2, [1, 2, 3]] # Pode-se se aninhar listas 

# Acessando valores de uma lista
print(notas[0])
print(notas[1])
print(notas[2])
print(notas[-1])

# Acessando um range
print(notas[0:3])
print(notas[:3])
print(notas[3:])
print(notas[0:-1:2])
print(notas[::2])

# For com lista

for elemento in notas:
    print(elemento)

for i in range(len(notas)): # range(5)
    print(i)

print("------------")

# Elementos de uma lista

print(len(notas))