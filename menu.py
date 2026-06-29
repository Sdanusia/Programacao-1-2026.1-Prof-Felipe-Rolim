from app.figurinha import ver_figurinhas, adicionar_figurinha, remover_figurinha
from app.troca import pedir_troca, ver_pedidos


def menu_usuario(usuario):
    while True:
        print("\n=== MENU DA CONTA ===")
        print("Usuário:", usuario)
        print("1 - Ver minhas figurinhas")
        print("2 - Adicionar figurinha")
        print("3 - Remover figurinha")
        print("4 - Pedir troca")
        print("5 - Pedidos recebidos")
        print("6 - Sair da conta")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_figurinhas(usuario)

        elif opcao == "2":
            adicionar_figurinha(usuario)

        elif opcao == "3":
            remover_figurinha(usuario)

        elif opcao == "4":
            pedir_troca(usuario)

        elif opcao == "5":
            ver_pedidos(usuario)

        elif opcao == "6":
            print("Saindo da conta...")
            break

        else:
            print("Opção inválida.")