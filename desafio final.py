# Criar um menu de usuário com 3 funções a saber:
### 1 - Contar caracteres
### 2 - Contar letras "a"
### 3 - Substituir letras "a" por "@"
### 4 - Sair do programa

def contador_de_a():
    texto = input("Digite sempre: ")
    return f"A letra 'a' aparece {texto.count('a')} vezes na frase. "
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
    print("morrendo enquanto mama . . .")
    exit()

def menu_usuario():
    print("Morrendo enquanto mama . . .")
    print("""1 - contar caracteres
             2 - contar letras "a"
             3 - substituir letras "a" por "@"
             4 - sair do programa
""")

opcao = int(input("digite a opção desejada: "))
if opcao == 1:
    print(contador())
    menu_usuario()   

elif opcao == 2:
    print(contador_de_a())
    menu_usuario()

elif opcao == 3:
    print(replace_a())
    menu_usuario()

elif opcao == 4:
    sair_programa()

else:
    print("opção inválida.")
    menu_usuario()

menu_usuario()                        



