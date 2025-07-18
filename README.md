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

## 🤝 Como Contribuir

Contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

Se você tiver uma sugestão para melhorar este projeto, por favor, faça um "fork" do repositório e crie um "pull request". Você também pode simplesmente abrir uma "issue" com a tag "melhoria".

1.  Faça um Fork do projeto
2.  Crie uma Branch para sua feature (`git checkout -b feature/AmazingFeature`)
3.  Faça o Commit de suas alterações (`git commit -m 'Add some AmazingFeature'`)
4.  Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5.  Abra um Pull Request

Não se esqueça de dar uma estrela ao projeto! Obrigada novamente!

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✍️ Créditos e Citação

Se você utilizar este projeto em seus trabalhos, tutoriais ou em qualquer outro lugar, por favor, me dê os devidos créditos. Ficarei muito feliz em saber que meu trabalho foi útil para você!

Você pode me creditar da seguinte forma:

* **Projeto Original:** Bot de IA para Afiliados Shopee
* **Autor:** Sarah Fernanda David Cunha
* **Link do Repositório:** [https://github.com/sarahfernandadc/shopee-gemini-twitter-bot]

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sarahfernandadc/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sarahfernandadc)


---

## ⚠️ Aviso Legal

Este projeto foi desenvolvido para fins educacionais. O uso de APIs está sujeito aos termos de serviço e limites de taxa de cada plataforma (Shopee, Google, X/Twitter). Use com responsabilidade.
