from app.dados import usuarios
from app.figurinha import ver_figurinhas


def pedir_troca(usuario):
    print("\n=== PEDIR TROCA ===")

    figurinha = input("Qual figurinha você quer conseguir? ").lower()

    if figurinha == "":
        print("Digite o nome da figurinha.")
        return

    encontrou = False

    print("\nPessoas que têm essa figurinha:")

    for nome in usuarios:
        if nome != usuario:
            if figurinha in usuarios[nome]["figurinhas"]:
                print("-", nome)
                encontrou = True

    if encontrou == False:
        print("Ninguém tem essa figurinha.")
        return

    destino = input("\nDigite o nome da pessoa para pedir a troca: ").lower()

    if destino not in usuarios:
        print("Pessoa não encontrada.")
        return

    if destino == usuario:
        print("Você não pode pedir troca para você mesmo.")
        return

    if figurinha not in usuarios[destino]["figurinhas"]:
        print("Essa pessoa não possui essa figurinha.")
        return

    print("\nSuas figurinhas:")
    ver_figurinhas(usuario)

    oferecida = input("\nQual figurinha sua você oferece? ").lower()

    if oferecida not in usuarios[usuario]["figurinhas"]:
        print("Você não possui essa figurinha.")
        return

    pedido = {
        "de": usuario,
        "quer": figurinha,
        "oferece": oferecida
    }

    usuarios[destino]["pedidos"].append(pedido)

    print("Pedido de troca enviado!")


def ver_pedidos(usuario):
    print("\n=== PEDIDOS RECEBIDOS ===")

    pedidos = usuarios[usuario]["pedidos"]

    if len(pedidos) == 0:
        print("Nenhum pedido recebido.")
        return

    for pedido in pedidos:
        print("\nPedido de:", pedido["de"])
        print("Quer receber:", pedido["quer"])
        print("Oferece:", pedido["oferece"])

    nome = input("\nDigite o nome de quem enviou o pedido: ").lower()

    pedido_escolhido = ""

    for pedido in pedidos:
        if pedido["de"] == nome:
            pedido_escolhido = pedido

    if pedido_escolhido == "":
        print("Pedido não encontrado.")
        return

    print("\n1 - Aceitar")
    print("2 - Recusar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        aceitar_troca(usuario, pedido_escolhido)
        pedidos.remove(pedido_escolhido)

    elif opcao == "2":
        pedidos.remove(pedido_escolhido)
        print("Pedido recusado.")

    else:
        print("Opção inválida.")


def aceitar_troca(usuario, pedido):
    quem_pediu = pedido["de"]
    desejada = pedido["quer"]
    oferecida = pedido["oferece"]

    if desejada not in usuarios[usuario]["figurinhas"]:
        print("Você não possui mais essa figurinha.")
        return

    if oferecida not in usuarios[quem_pediu]["figurinhas"]:
        print("A outra pessoa não possui mais a figurinha oferecida.")
        return

    usuarios[usuario]["figurinhas"].remove(desejada)
    usuarios[quem_pediu]["figurinhas"].remove(oferecida)

    usuarios[usuario]["figurinhas"].append(oferecida)
    usuarios[quem_pediu]["figurinhas"].append(desejada)

    print("Troca aceita e realizada com sucesso!")