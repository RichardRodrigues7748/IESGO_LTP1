#Exercicio com range e if em python

#Crie um programa que solicite ao usuario inserir um numero inteiro positivo e o sistema retorna se ele é multiplo de 5 e retorne uma lista de todos os numeros positivos menores que o numero inserido que sao multiplos de 5.

def multiplos_de_5(numero):
    # Inicializa uma lista para armazenar os múltiplos de 5
    multiplos_de_5 = []

    # Verifica e armazena todos os múltiplos de 5 menores que o número inserido
    for i in range(1, numero):
        if i % 5 == 0:
            multiplos_de_5.append(i)

    # Verifica se o número inserido é múltiplo de 5
    if numero % 5 == 0:
        print(f"{numero} é um múltiplo de 5.")
    else:
        print(f"{numero} não é um múltiplo de 5.")

    # Retorna a lista de múltiplos de 5
    return multiplos_de_5

# Solicita ao usuário inserir um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Chama a função e imprime a lista de múltiplos de 5
resultado = multiplos_de_5(numero)
print(f"Lista de múltiplos de 5 menores que {numero}: {resultado}")