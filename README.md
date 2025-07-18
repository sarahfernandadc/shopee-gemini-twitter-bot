# 🤖 Bot de IA para Afiliados Shopee

Um bot em Python que utiliza a IA do Google (Gemini) para automatizar completamente o processo de marketing de afiliados da Shopee, desde a descoberta de produtos até a postagem no X (Twitter).

## ✨ Funcionalidades

-   **Interface Interativa:** O bot pergunta o tema da busca e a quantidade de posts a serem publicados no início da execução.
-   **Geração de Palavras-Chave com IA:** A partir de um tema geral (ex: "setup gamer pink"), a IA sugere palavras-chave específicas e eficazes para encontrar os melhores produtos.
-   **Criação de Conteúdo com IA:** Gera textos de tweets chamativos e formatados para cada produto, prontos para engajar seu público.
-   **Postagem Automatizada:** Baixa a imagem do produto e posta o tweet com a imagem e seu link de afiliado diretamente no seu perfil do X.
-   **Segurança:** Gerencia suas chaves de API de forma segura através de um arquivo `.env`, que não é enviado para o repositório.

## 📂 Estrutura do Projeto

```
shopee-ai-bot/
├── src/
│   ├── __init__.py
│   ├── shopee_api.py
│   ├── gemini_handler.py
│   ├── twitter_handler.py
│   ├── user_interaction.py
│   └── main.py
│
├── .env
├── requirements.txt
└── LEIAME.md
```

## 🚀 Instalação e Execução

Siga os passos abaixo para colocar o bot para funcionar.

### Pré-requisitos
- Python 3.8+
- Git

### Passos

1.  **Clone o Repositório**

2.  **Crie e Ative o Ambiente Virtual**
    ```bash
    # Cria o ambiente
    python -m venv venv

    # Ativa o ambiente (Windows)
    .\venv\Scripts\activate

    # Ativa o ambiente (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Chaves de API**
    - Crie um arquivo chamado `.env` na pasta principal do projeto.
    - Copie o conteúdo do arquivo `.env.example` para o arquivo `.env` criado e substitua os valores pelas suas chaves reais.

## ▶️ Como Usar

Com tudo configurado, execute o script principal a partir do terminal:

```bash
python src/main.py
```

O bot irá solicitar o **tema da busca** e a **quantidade de posts**. Após fornecer as informações, o processo de automação começará.

## ⚠️ Aviso Legal
Este projeto foi desenvolvido para fins educacionais. O uso de APIs está sujeito aos termos de serviço e limites de taxa de cada plataforma (Shopee, Google, X/Twitter). Use com responsabilidade.
