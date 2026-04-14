import random
import string

def gerar_senha(tamanho=8, usar_numeros=True, usar_simbolos=True):
    caracteres = string.ascii_letters

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha