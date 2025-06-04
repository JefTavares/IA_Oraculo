import streamlit as st

MENSAGENS_EXEMPLO = [
    ("user", "Olá"),
    ("assistant", "Tudo bem?"),
    ("user", "Olá, tudo otimo!"),
]


def pagina_chat():
    st.header("🤖Bem-vindo ao Oráculo", divider=True)

    # Memoria dentro do aplicativo streamlit. se não tiver uma sessão, cria uma nova ("mensagens", [])
    mensagens = st.session_state.get("mensagens", MENSAGENS_EXEMPLO)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])
        # Se for a mensagem do usuário, mostra o campo de entrada

    input_usuario = st.chat_input("Fale com o oráculo")
    # se tem input do usuario.
    print(input_usuario)
    if input_usuario:
        mensagens.append(("user", input_usuario))  # Adiciona a mensagem do usuário
        st.session_state["mensagens"] = mensagens  # Atualiza a sessão com as mensagens
        st.rerun()  # Recarrega a página para mostrar a nova mensagem


def main():
    pagina_chat()


if __name__ == "__main__":
    main()
