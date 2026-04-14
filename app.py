from senha import gerar_senha
import os

def menu():
    while True:
        print("\n--- GERADOR DE SENHAS ---")
        print("1 - Gerar senha")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            tamanho = int(input("Tamanho da senha: "))
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")

        elif opcao == "0":
            break

if __name__ == "__main__":
    if os.getenv("CI"):
        print("CI executado com sucesso!")
    else:
        print("Senha gerada automaticamente:", gerar_senha(10))