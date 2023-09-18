# Método split() e método strip():
# O método split() divide o string em uma lista de strings, separando por um delimitador.
# Exemplo:

def seletor_de_nome():
    nome_completo = input("Digite seu nome e sobrenome: ")
    nome_completo = nome_completo.title().split()
    primeiro_nome = nome_completo[0]
    ultimo_nome = nome_completo[-1]
    return f"Seu primeiro nome é {primeiro_nome} e seu último nome é {ultimo_nome}. "
print(seletor_de_nome())

# Exemplo:

def remover_espaços():
    nome = input("Digite nosso nome: ")
    return nome.strip()
print(remover_espaços())

# Exemplo de uso do split() e strip() juntos:
# Suponha uma lista de usuários que estão cadastrados no sistema. Crie um programa que separe os usuários;
# E exiba apenas o nome do usuário.

def lista_de_usuarios():
    lista_de_usuarios = ["THIAGO", "DANIBOY", "PINGUIM", "GABRIEL"]
    usuario_selecionado = int(input("Digite a colocação do usuário: "))
    usuario_selecionado = lista_de_usuarios [usuario_selecionado - 2].strip().split()
    return usuario_selecionado[0]
print(lista_de_usuarios())

# Criar um menu de usuário com 3 funções a saber:
### 1 - Contar caracteres
### 2 - Contar letras "a"
### 3 - Substituir letras "a" por "@"
### 4 - Sair do programa

def menu_usuario():
    print("Morrendo enquanto mama . . .")
    print("")

def contador_de_a():
    texto = input("Digite sempre: ")
    return f"A letra 'p' aparece {texto.count('a')} vezes na frase. "
print (contador_de_a()) 

def contador():
    frase = input("Digite ali: ")
    return len(frase)
print(contador())

def replace_a():
    frase = input("digite uma frase/palavra")
    return frase.replace("a" , "@")
print(replace_a())

def sair_programa():
    print("saindo do programa . . .")
    exit()

    