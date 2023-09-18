# String Methods

# Exemplo de método replace()
# Crie uma função que solicite ao usuário digitar uma frase e substitua todas as letras "a" por "@"
# E exiba a nova frase na tela.

def replace_a():
    frase = input("digite uma frase/palavra")
    return frase.replace("a" , "super sexo")
print(replace_a())

# Exemplo de método: Len() para contar o tamanho da string
def tamanho_do_texto(texto):
    return len(texto)

print(tamanho_do_texto("dudu mongooo")) 

# Cria um contador de caracteres em que o usuário digite uma frase e o programa exiba quantas

def contador():
    frase = input("Digite ali: ")
    return len(frase)
print(contador())

# Usar o método count() para contar quantas vezes uma letra aparece na frase.

def contador_de_p():
    texto = input("Digite sempre: ")
    return f"A letra 'p' aparece {texto.count('p')} vezes na frase. "
print (contador_de_p())    

# Desafio: Qual é a diferença entre o método capitalize() e o metodo title()
# Capitalize () deixa a primeira letra em maiúscula.
# title () deixa a primeira letra de cada palavra maiúscula.

# Desafio: Qual é a diferença entre o método upper() e o método swapcase()?

def text():
    frase = input("Digite ali? ")
    return upper(frase)
print(text())

#R: upper() deixa todas as letras da frase em maiúscula.
#R: Lower() deixa todas as letras da frase em minuscula.
#R: Swapcase() deixa todas as letras maiúscula e minusculas e vice-versa.


