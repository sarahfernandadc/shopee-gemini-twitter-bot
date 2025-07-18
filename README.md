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

## 🌟 Pontos a Melhorar e Próximos Passos

Este projeto é um trabalho em andamento e há sempre espaço para melhorias. As contribuições são muito bem-vindas!

É importante mencionar que este projeto também é uma **jornada de aprendizado** para mim. Estou aplicando e descobrindo novas técnicas ao longo do desenvolvimento. Portanto, se você tiver sugestões de abordagens mais eficientes, conhecer padrões de projeto melhores ou enxergar pontos onde o código pode ser aprimorado, sua contribuição será especialmente valiosa. O objetivo é aprender e construir em comunidade!

Abaixo estão algumas ideias para o futuro do bot:

**1. Interface Gráfica ou Web para Configuração Inicial**
* **Problema:** Atualmente, a configuração das chaves de API e outros parâmetros exige que o usuário edite manualmente o arquivo `.env`. Isso pode ser uma barreira para pessoas sem afinidade com programação.
* **Melhoria:** Desenvolver uma interface de usuário simples onde o usuário possa inserir e salvar suas chaves de API de forma segura e intuitiva, sem tocar em arquivos de configuração.

**2. Customização de Templates de Tweet**
* **Problema:** O formato dos tweets é fixo no código, o que limita a criatividade e a capacidade do usuário de adaptar o conteúdo à sua própria voz ou nicho.
* **Melhoria:** Permitir que os usuários criem e salvem seus próprios modelos de tweet. Isso poderia ser feito através de um campo na interface gráfica, onde o usuário definiria o texto usando variáveis como `{produto}`, `{link_afiliado}`, `{preco}`, `{hashtags_ia}`.

**3. Agendamento de Postagens**
* **Ideia:** Em vez de rodar o bot manualmente, o usuário poderia configurar um agendamento para que as postagens sejam feitas automaticamente em horários específicos (ex: "postar 3 vezes ao dia").
* **Implementação:** Integrar uma biblioteca de agendamento para gerenciar os posts de forma autônoma.

**4. Filtros Avançados de Produtos**
* **Ideia:** Dar mais controle ao usuário sobre os tipos de produtos que são selecionados, além da palavra-chave.
* **Melhoria:** Adicionar opções na interface para filtrar produtos por faixa de preço, avaliação mínima (número de estrelas), ou popularidade (número de vendas).

**5. Suporte a Múltiplas Plataformas**
* **Ideia:** Expandir o alcance do bot para além do X (Twitter).
* **Melhoria:** Refatorar o código de postagem para uma estrutura modular, permitindo adicionar facilmente outros "handlers" para postar em diferentes redes sociais, como Telegram, Facebook ou Pinterest.

**6. Melhoria na Robustez e Logs**
* **Ideia:** Tornar o bot mais resiliente a falhas (ex: API da Shopee temporariamente fora do ar).
* **Melhoria:** Implementar um sistema de logs para registrar as atividades e os erros.

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
