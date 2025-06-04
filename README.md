# IA Oráculo

Um assistente conversacional inteligente construído com [Streamlit](https://streamlit.io/) e [Langchain](https://python.langchain.com/), capaz de interagir com o usuário, processar diferentes tipos de arquivos (Site, Youtube, PDF, CSV, TXT) e utilizar múltiplos modelos de linguagem (Groq, OpenAI).

## Funcionalidades

- Interface web interativa com Streamlit.
- Chat com histórico de mensagens.
- Upload e leitura de arquivos: PDF, CSV, TXT.
- Suporte a URLs de sites e vídeos do Youtube.
- Seleção de provedores e modelos de linguagem (Groq, OpenAI).
- Armazenamento de chaves de API por provedor.
- Memória de sessão para histórico de conversas.

## Requisitos

- Python 3.11+
- [Streamlit](https://streamlit.io/)
- [Langchain](https://python.langchain.com/)
- Outras dependências listadas em `pyproject.toml`

## Instalação

Clone o repositório e instale as dependências:

```sh
git clone https://github.com/seu-usuario/ia-oraculo.git
cd ia-oraculo
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -e .
```

Ou instale diretamente via pip:

```sh
pip install -r requirements.txt
```

## Como usar

Execute a aplicação principal com Streamlit:

```sh
streamlit run 03_aula.py
```

Acesse a interface web pelo navegador, normalmente em http://localhost:8501.

## Estrutura do Projeto

- `03_aula.py`: Interface principal do chat e sidebar para upload/modelos.
- `02_aula.py`: Versão simplificada do chat.
- `main.py`: Script de exemplo/entrada.
- `.vscode/`: Configurações para desenvolvimento no VS Code.
- `pyproject.toml`: Dependências e metadados do projeto.

## Configuração de APIs

Para utilizar modelos de linguagem, adicione suas chaves de API na barra lateral da interface, conforme solicitado para cada provedor.

## Licença

Este projeto está sob a licença MIT.

---

Desenvolvido com ❤️ usando Streamlit e Langchain.