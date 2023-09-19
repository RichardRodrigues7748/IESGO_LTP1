# Solicite ao usuario nome e sobrenome e retorne um usuario para login com as tres primeiras letras do nome e as tres primeiras letras do sobrenome.

# Solicita ao usuário o nome e sobrenome
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Pega as três primeiras letras do nome e sobrenome
primeiras_letras_nome = nome[:3]
primeiras_letras_sobrenome = sobrenome[:3]

# Cria o nome de usuário
nome_usuario = primeiras_letras_nome + primeiras_letras_sobrenome

# Imprime o nome de usuário
print("Seu nome de usuário é:", nome_usuario)




# Dicionário simulando dados de usuários (nome de usuário e senha)
dados_usuarios = {
    "josilva": "senha123",
    "anapere": "abc456",
    "luizfer": "qwerty",
    # Adicione mais usuários conforme necessário
}

# Solicita ao usuário o nome e sobrenome
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Pega as três primeiras letras do nome e sobrenome
primeiras_letras_nome = nome[:3]
primeiras_letras_sobrenome = sobrenome[:3]

# Cria o nome de usuário
nome_usuario = primeiras_letras_nome + primeiras_letras_sobrenome

# Verifica se o nome de usuário existe no dicionário de dados de usuários
if nome_usuario in dados_usuarios:
    senha = input("Digite sua senha: ")
    if senha == dados_usuarios[nome_usuario]:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta. Tente novamente.")
else:
    print("Nome de usuário não encontrado. Registre-se primeiro.")
