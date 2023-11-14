# Funções

def saudacao():
    print("Seja bem vindo")
    print("Aproveite a leitura do codigo")

saudacao()

# Com parametros

def sauadcao2(nome):
    print("Seja bem vindo", nome)

sauadcao2("Bruno")

def saudacao3(nome, linguagem="Python"):
    print("Seja bem vindo", nome)
    print("Você está estudando", linguagem)

saudacao3("Bruno")
saudacao3("Bruno", "JS")

# Com retornos

def soma(a, b):
    return a + b;

print(soma(1,2))