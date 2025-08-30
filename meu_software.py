def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo ao software."

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    if not nome.strip():
        nome = "Usuário"
    print(saudacao(nome))
