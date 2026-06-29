from app.dados import usuarios


def ver_figurinhas(usuario):
    print("\n=== MINHAS FIGURINHAS ===")

    if len(usuarios[usuario]["figurinhas"]) == 0:
        print("Nenhuma figurinha cadastrada.")
    else:
        for figurinha in usuarios[usuario]["figurinhas"]:
            print("-", figurinha)


def adicionar_figurinha(usuario):
    print("\n=== ADICIONAR FIGURINHA ===")

    figurinha = input("Nome do jogador da figurinha: ").lower()

    if figurinha == "":
        print("Nome inválido.")
        return

    if figurinha in usuarios[usuario]["figurinhas"]:
        print("Essa figurinha já foi cadastrada.")
    else:
        usuarios[usuario]["figurinhas"].append(figurinha)
        print("Figurinha adicionada com sucesso!")


def remover_figurinha(usuario):
    print("\n=== REMOVER FIGURINHA ===")

    ver_figurinhas(usuario)

    figurinha = input("Digite o nome da figurinha que deseja remover: ").lower()

    if figurinha in usuarios[usuario]["figurinhas"]:
        usuarios[usuario]["figurinhas"].remove(figurinha)
        print("Figurinha removida com sucesso!")
    else:
        print("Você não possui essa figurinha.")