import os
import time
from dotenv import load_dotenv

from shopee_api import ShopeeClient
from gemini_handler import generate_keywords, create_tweet_content
from twitter_handler import post_tweet_with_image
from user_interaction import get_search_theme, get_post_quantity

# --- Constants ---
# Time to wait between posts to avoid API rate limits (in seconds)
POST_INTERVAL_SECONDS = 180
# Shopee sorting type: 2 for relevance, 4 for top sales
SHOPEE_SORT_TYPE = 2

def main():
    """
    Main function to run the Shopee Affiliate Bot.
    """
    print("=" * 60)
    print("🚀 Welcome to the Shopee Affiliate AI Bot 🚀")
    print("=" * 60)

    # 1. Load credentials from .env file
    load_dotenv()
    credentials = {
        "SHOPEE_APP_ID": os.getenv("SHOPEE_APP_ID"),
        "SHOPEE_SECRET_KEY": os.getenv("SHOPEE_SECRET_KEY"),
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        "TWITTER": {
            "API_KEY": os.getenv("API_KEY"),
            "API_KEY_SECRET": os.getenv("API_KEY_SECRET"),
            "ACCESS_TOKEN": os.getenv("ACCESS_TOKEN"),
            "ACCESS_TOKEN_SECRET": os.getenv("ACCESS_TOKEN_SECRET"),
        }
    }
    # Validate that all keys are present
    if not all(credentials.values()) or not all(credentials["TWITTER"].values()):
        print("❌ CRITICAL ERROR: One or more API keys are missing from your .env file.")
        return

    # 2. Get user input
    search_theme = get_search_theme()
    posts_to_publish = get_post_quantity()

    # 3. Initialize API Clients
    shopee_client = ShopeeClient(credentials["SHOPEE_APP_ID"], credentials["SHOPEE_SECRET_KEY"])

    # 4. Generate search keywords with AI
    keywords = generate_keywords(search_theme, credentials["GEMINI_API_KEY"], count=posts_to_publish)

    # 5. Main processing loop
    posts_published_count = 0
    for i, keyword in enumerate(keywords):
        if posts_published_count >= posts_to_publish:
            print("\n🏁 Desired number of posts has been published. Halting.")
            break
        
        print("-" * 60)
        print(f"Processing Post #{posts_published_count + 1}/{posts_to_publish} (Keyword: '{keyword}')")
        
        products = shopee_client.search_products(keyword, limit=1, sort_type=SHOPEE_SORT_TYPE)

        if not products or not products[0].get("offerLink"):
            print("   ⏩ Skipping this keyword as no valid product was found.")
            continue

        selected_product = products[0]

        # Generate tweet content
        tweet_text = create_tweet_content(selected_product, credentials["GEMINI_API_KEY"])

        # Post to Twitter
        success = post_tweet_with_image(tweet_text, selected_product["imageUrl"], credentials["TWITTER"])
        
        if success:
            posts_published_count += 1
            if posts_published_count < posts_to_publish:
                print(f"   ⏳ Pausing for {POST_INTERVAL_SECONDS} seconds to respect API limits...")
                time.sleep(POST_INTERVAL_SECONDS)
        else:
            print("   ⏩ Failed to post. Moving to the next keyword.")
            time.sleep(10) # Short pause after a failure

    print("\n" + "=" * 60)
    print("🎉 Automation process finished! 🎉")
    print(f"Total posts successfully published: {posts_published_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()