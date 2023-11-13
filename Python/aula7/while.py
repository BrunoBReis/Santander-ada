# Estrutura do while

numero_sorteado = 42

# Escolhendo um valor impossível para o numero escolhido
numero_escolhido = -1

# Enquanto o número escolhido for diferente 
while (numero_escolhido != numero_sorteado):
    numero_escolhido = int(input("Escolha um número: "))

    # Usanod o if para não printar o "Você errou"
    if (numero_escolhido == numero_sorteado):
        break

    print("Voce errou")

print("Voce acertou")

contador = 0

while (contador < 5):
    # Conando do 1 a 5
    print(contador + 1)
    contador += 1