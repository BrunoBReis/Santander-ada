# Metodos da lista

lista = [1, 3, 12, 8, 2]

# Append
lista.append(3)

print(lista)

# Insert
lista.insert(0, 2)

print(lista)

# Extend
lista2 = [1 ,2, 3]

lista.extend(lista2)

print(lista)

# Pop
lista.pop(-1)

print(lista)

# Remove (a primeira aparicao do numero)
lista.remove(2)

print(lista)

# Count
print(lista.count(1))

# Index
print(lista.index(1))

# Sort
lista.sort() # reverse=True
print(lista)

# Funcoes

# Len
print(len(lista))

# Sum
print(sum(lista))

# Max
print(max(lista))

# Min
print(min(lista))