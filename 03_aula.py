import streamlit as st

# CONSTANTES - Para organização de código
TIPOS_ARQUIVOS_VALIDOS = ["Site", "Youtube", "Pdf", "Csv", "Txt"]

CONFIG_MODELOS = {
    "Groq": {
        "modelos": ["llama-3.1-70b-versatile", "gemma2-9b-it", "mixtral-8x7b-32768"]
    },
    "OpenAI": {"modelos": ["gpt-4o-mini", "gpt-4o", "o1-preview", "o1-mini"]},
}

CONFIG_MODELOS = {
    "Groq": {
        "modelos": ["llama-3.1-70b-versatile", "gemma2-9b-it", "mixtral-8x7b-32768"]
    },
    "OpenAI": {"modelos": ["gpt-4o-mini", "gpt-4o", "o1-preview", "o1-mini"]},
}

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


def sidebar():
    tabs = st.tabs(["Upload de Arquivos", "Seleção de Modelos"])
    # tudo que eu escrever dentro do with vai aparecer na aba "Upload de Arquivos"
    with tabs[0]:
        tipo_arquivo = st.selectbox(
            "Selecione o tipo de arquivo", TIPOS_ARQUIVOS_VALIDOS
        )
        if tipo_arquivo == "Site":
            arquivo = st.text_input("Digite a url do site")
        if tipo_arquivo == "Youtube":
            arquivo = st.text_input("Digite a url do vídeo")
        if tipo_arquivo == "Pdf":
            arquivo = st.file_uploader("Faça o upload do arquivo pdf", type=[".pdf"])
        if tipo_arquivo == "Csv":
            arquivo = st.file_uploader("Faça o upload do arquivo csv", type=[".csv"])
        if tipo_arquivo == "Txt":
            arquivo = st.file_uploader("Faça o upload do arquivo txt", type=[".txt"])

    with tabs[1]:
        provedor = st.selectbox(
            "Selecione o provedor dos modelo",
            CONFIG_MODELOS.keys(),  # pega s keys do dicionário CONFIG_MODELOS
        )

        modelo = st.selectbox("Selecione o modelo", CONFIG_MODELOS[provedor]["modelos"])

        api_key = st.text_input(
            f"Adicione a api key para o provedor {provedor}",
            value=st.session_state.get(f"api_key_{provedor}"),
        )

        st.session_state[f"api_key_{provedor}"] = api_key


def main():
    pagina_chat()
    with st.sidebar:
        sidebar()


if __name__ == "__main__":
    main()
