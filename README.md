# Shopee Affiliate Twitter Bot com IA

Este é um bot em Python que utiliza a IA do Google (Gemini) para automatizar a criação e postagem de tweets de marketing de afiliados para produtos da Shopee.

## Funcionalidades

-   **Estratégia com IA:** Usa a Gemini para gerar palavras-chave de busca relevantes a partir de um tema geral (ex: "setup gamer").
-   **Busca de Produtos:** Conecta-se à API de Afiliados da Shopee para encontrar produtos populares.
-   **Criação de Conteúdo com IA:** Gera textos de tweets chamativos e formatados, prontos para postar.
-   **Automação de Postagem:** Baixa a imagem do produto e posta o tweet com a imagem e o link de afiliado diretamente no seu perfil do X (Twitter).
-   **Altamente Configurável:** Todos os parâmetros de busca e postagem podem ser ajustados facilmente.

## Instalação e Configuração

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/seu-usuario/seu-projeto-shopee-bot.git](https://github.com/seu-usuario/seu-projeto-shopee-bot.git)
    cd seu-projeto-shopee-bot
    ```

2.  **Instale as Dependências**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure suas Chaves de API**
    -   Renomeie o arquivo `.env.example` para `.env`.
    -   Abra o arquivo `.env` e preencha com suas chaves da **Shopee Affiliate API**, **Google AI Studio (Gemini)** e **Twitter Developer API**.

4.  **Ajuste os Parâmetros**
    -   Abra o arquivo `src/config.py` para definir o tema da busca, a quantidade de posts e o intervalo entre eles.

## Como Usar

Após a configuração, basta executar o script principal:

```bash
python src/main.py
```

O bot começará o processo e você verá o log de atividades no terminal.

## Aviso Legal

Este projeto é para fins educacionais. O uso de APIs está sujeito aos termos de serviço e limites de taxa de cada plataforma (Shopee, Google, X/Twitter). Use com responsabilidade.