from app.database import buscar_contatos
from app.whatsapp import enviar_mensagem


def main():

    contatos = buscar_contatos()


    if not contatos:

        print("Nenhum contato encontrado.")
        return


    for contato in contatos:

        nome = contato["nome_contato"]
        telefone = contato["telefone"]


        enviar_mensagem(
            telefone,
            nome
        )


if __name__ == "__main__":
    main()