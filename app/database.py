from supabase import create_client

from app.config import SUPABASE_URL, SUPABASE_KEY


supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def buscar_contatos():

    try:
        resposta = (
            supabase
            .table("contatos")
            .select("*")
            .limit(3)
            .execute()
        )

        return resposta.data

    except Exception as erro:
        print(f"Erro ao buscar contatos: {erro}")
        return []