# Dicionario

dicionario = {}
dicionario = dict()

dicionario = {"nome": "Bruno", "idade": 21, "altura": 1.75}

print(dicionario)

print(dicionario["nome"])

# Adicionando elementos

dicionario["programador"] = True
print(dicionario["programador"])

dicionario["altura"] = 1.80
print(dicionario)

# Usando for 

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existencia de chave

print("nome" in dicionario)