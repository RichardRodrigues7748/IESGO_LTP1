# Exercício 09 - Crie uma aplicação que solicita ao usuário que digite um texto e imprima no console o texto digitado pelo usuário sem nenhuma vogal.

def apg_vogais():
    frase = input("Digite uma palavra ")
    return frase.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print(apg_vogais())

# Exercício 10 - Crie uma aplicação que solicita ao usuário que digite um texto e retorne a quantidade de caracteres que o texto possui.

def quantidade_caracteres(texto):
    texto_sem_espaca = texto.lower().replace(' ', '')
    return len(texto_sem_espaca)
 
    
print(" Esse texto possui ",quantidade_caracteres(input(" Digite texto ")), " caracter's")
