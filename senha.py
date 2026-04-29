import random
import string

def gerar_senha(tamanho=8, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters

    senha = []

    if usar_numeros:
        caracteres += string.digits
        senha.append(random.choice(string.digits))

    if usar_simbolos:
        caracteres += string.punctuation
        senha.append(random.choice(string.punctuation))

    # Preenche o restante da senha
    while len(senha) < tamanho:
        senha.append(random.choice(caracteres))

    random.shuffle(senha)

    return ''.join(senha)