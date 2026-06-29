from app.dados import usuarios


def criar_conta():
    print("\n=== CRIAR CONTA ===")

    nome = input("Nome de usuário: ").lower()

    if nome == "":
        print("O nome não pode ficar vazio.")
        return

    if nome in usuarios:
        print("Esse usuário já existe.")
        return

    senha = input("Senha: ")

    if senha == "":
        print("A senha não pode ficar vazia.")
        return

    usuarios[nome] = {
        "senha": senha,
        "figurinhas": [],
        "pedidos": []
    }

    print("Conta criada com sucesso!")


def entrar():
    print("\n=== LOGIN ===")

    nome = input("Usuário: ").lower()
    senha = input("Senha: ")

    if nome in usuarios:
        if usuarios[nome]["senha"] == senha:
            print("Login realizado com sucesso!")
            return nome

    print("Usuário ou senha incorretos.")
    return ""