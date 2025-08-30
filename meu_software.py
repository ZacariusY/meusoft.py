def saudacao(nome):
    return f"OLÁ, {nome.upper()}! BEM-VINDO AO SOFTWARE."

if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    if not nome.strip():
        nome = "Usuário"
    print(saudacao(nome))
