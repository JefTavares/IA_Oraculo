from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    CSVLoader,
    PyPDFLoader,
    TextLoader,
)

url = "http://www.guiadosquadrinhos.com/capas/magico-vento-deluxe/ma062110"

loader = WebBaseLoader(url)  # faz o scrapping
lista_documentos = loader.load()  # carrega
print(lista_documentos)

documento = "\n\n".join([doc.page_content for doc in lista_documentos])

print(documento)


def carrega_site(url):
    loader = WebBaseLoader(url)  # faz o scrapping
    lista_documentos = loader.load()  # carrega
    # pega apenas o page content da página
    documento = "\n\n".join([doc.page_content for doc in lista_documentos])
    return documento


video_id = "Ibx1SPuKziM"
loader = YoutubeLoader(video_id, add_video_info=False, language=["pt"])
lista_documentos_yt = loader.load()
documento = "\n\n".join([doc.page_content for doc in lista_documentos_yt])

print(documento)


# Pega a transcrição dos videos do youtube
def carrega_youtube(video_id):
    loader = YoutubeLoader(video_id, add_video_info=False, language=["pt"])
    lista_documentos = loader.load()
    documento = "\n\n".join([doc.page_content for doc in lista_documentos])
    return documento


def carrega_csv(caminho):
    loader = CSVLoader(caminho)
    lista_documentos = loader.load()
    documento = "\n\n".join([doc.page_content for doc in lista_documentos])
    return documento


caminho = "arquivos/knowledge_base.csv"
documento = carrega_csv(caminho)
print(documento)


def carrega_pdf(caminho):
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = "\n\n".join([doc.page_content for doc in lista_documentos])
    return documento


caminho = "arquivos/RoteiroViagemEgito.pdf"
documento = carrega_pdf(caminho)
print(documento)


def carrega_txt(caminho):
    loader = TextLoader(caminho)
    lista_documentos = loader.load()
    documento = "\n\n".join([doc.page_content for doc in lista_documentos])
    return documento


caminho = "arquivos/knowledge_base.txt"
documento = carrega_txt(caminho)
print(documento)
