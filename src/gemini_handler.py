import google.generativeai as genai
import json

def generate_keywords(theme: str, api_key: str, count: int = 10) -> list[str]:
    """
    Uses Gemini AI to generate a list of effective search keywords from a general theme.

    Args:
        theme: The general theme (e.g., "home office setup").
        api_key: The API key for Google Gemini.
        count: The number of keywords to generate.

    Returns:
        A list of keywords, or a list with the original theme as a fallback.
    """
    print(f"🧠 Using AI to generate {count} keywords for the theme: '{theme}'...")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
    Aja como um especialista em SEO para e-commerce da Shopee. Meu objetivo é encontrar produtos relacionados ao tema: "{theme}".

    Gere uma lista com {count} palavras-chave específicas e eficazes para busca, que eu possa usar na API da Shopee para encontrar produtos relevantes e populares.

    Retorne sua resposta SOMENTE como um array JSON válido. Não inclua nenhum outro texto, explicações ou markdown como ```json. Apenas o array.

    Exemplo de resposta para o tema "home office":
    ["cadeira ergonômica para escritório", "luminária de mesa led sem fio", "mousepad grande para jogos", "organizador de cabos"]
    """
    generation_config = genai.types.GenerationConfig(response_mime_type="application/json")
    
    try:
        response = model.generate_content(prompt, generation_config=generation_config)
        keywords = json.loads(response.text)
        print("   ✅ Keywords generated successfully.")
        return keywords
    except Exception as e:
        print(f"❌ Error generating keywords with Gemini: {e}")
        print("   Falling back to using the original theme as the only keyword.")
        return [theme]


def create_tweet_content(product: dict, api_key: str) -> str:
    """
    Uses Gemini AI to generate a catchy tweet for a given product.

    Args:
        product: A dictionary containing product details from Shopee.
        api_key: The API key for Google Gemini.

    Returns:
        A formatted string for the tweet.
    """
    print(f"   ✍️ Generating tweet content for '{product.get('productName')[:40]}...'")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    Você é um gerente de redes sociais especializado em encontrar os melhores achados ("achadinhos") para um perfil no X (Twitter).
    Crie o conteúdo para um único TWEET sobre o produto abaixo.
    Retorne sua resposta SOMENTE como um objeto JSON válido com uma única chave "catchphrase", sem nenhum texto adicional.

    **Produto:**
    - Nome: {product.get('productName')}
    - Preço: R$ {product.get('priceMin')}

    **Exemplo de saída JSON:**
    {{
      "catchphrase": "🎯 Oferta imperdível! Não perca!"
    }}

    **Instruções para o conteúdo:**
    1.  `catchphrase`: Crie UMA frase curta e chamativa para o início do tweet. Use 1 ou 2 emojis que combinem com a ideia de "achado" ou "promoção".
    """
    generation_config = genai.types.GenerationConfig(response_mime_type="application/json")
    
    try:
        response = model.generate_content(prompt, generation_config=generation_config)
        data = json.loads(response.text)
        catchphrase = data.get("catchphrase", "🎯 Amazing deal alert!")
    except Exception as e:
        print(f"      ❌ Error generating tweet with Gemini: {e}. Using a default catchphrase.")
        catchphrase = "🎯 Amazing deal alert!"
        
    # Assemble the final tweet
    price_formatted = f"{float(product.get('priceMin', 0)):.2f}".replace('.', ',')
    tweet_text = (
        f"{catchphrase}\n\n"
        f"🔥 {product.get('productName')}\n\n"
        f"💲 For R$ {price_formatted}\n\n"
        f"🛒 Shop now 👉 {product.get('offerLink')}\n\n"
        f"⚠️ Don't miss it! ⚠️"
    )
    return tweet_text