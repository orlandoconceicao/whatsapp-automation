import requests

from app.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    ZAPI_CLIENT_TOKEN
)


def enviar_mensagem(
    telefone,
    nome_contato
):

    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/send-text"
    )


    mensagem = (
        f"Olá, {nome_contato} tudo bem com você?"
    )


    dados = {
        "phone": telefone,
        "message": mensagem
    }


    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN
    }


    try:

        resposta = requests.post(
            url,
            json=dados,
            headers=headers
        )


        print(resposta.json())


    except Exception as erro:

        print(
            f"Erro ao enviar mensagem: {erro}"
        )