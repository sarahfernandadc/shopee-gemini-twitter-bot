import requests
import tweepy
import os

def _download_image(image_url: str, local_filename: str = "temp_image.jpg") -> str | None:
    """Downloads an image from a URL and saves it locally."""
    try:
        print(f"   📥 Downloading image from: {image_url[:60]}...")
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)
        print(f"      Image saved as '{local_filename}'.")
        return local_filename
    except requests.exceptions.RequestException as e:
        print(f"      ❌ ERROR: Failed to download image. Reason: {e}")
        return None

def post_tweet_with_image(tweet_text: str, image_url: str, credentials: dict) -> bool:
    """
    Uploads an image and posts a tweet to X (Twitter).

    Args:
        tweet_text: The text content of the tweet.
        image_url: The URL of the image to attach.
        credentials: A dictionary with Twitter API keys.

    Returns:
        True if the post was successful, False otherwise.
    """
    local_image_path = _download_image(image_url)
    if not local_image_path:
        return False

    try:
        # Authenticate using v2 client for posting
        client_v2 = tweepy.Client(
            consumer_key=credentials['API_KEY'],
            consumer_secret=credentials['API_KEY_SECRET'],
            access_token=credentials['ACCESS_TOKEN'],
            access_token_secret=credentials['ACCESS_TOKEN_SECRET']
        )
        # Authenticate using v1.1 API for media upload
        auth_v1 = tweepy.OAuth1UserHandler(
            consumer_key=credentials['API_KEY'],
            consumer_secret=credentials['API_KEY_SECRET'],
            access_token=credentials['ACCESS_TOKEN'],
            access_token_secret=credentials['ACCESS_TOKEN_SECRET']
        )
        api_v1 = tweepy.API(auth_v1)

        print(f"   📤 Uploading '{local_image_path}' to X...")
        media = api_v1.media_upload(filename=local_image_path)
        media_id = media.media_id_string
        print(f"      Upload complete. Media ID: {media_id}")

        print("   🚀 Posting tweet...")
        response = client_v2.create_tweet(text=tweet_text, media_ids=[media_id])
        
        tweet_id = response.data['id']
        print(f"   ✅ SUCCESS! Tweet posted: [https://x.com/user/status/](https://x.com/user/status/){tweet_id}")
        return True

    except tweepy.errors.TooManyRequests:
        print("   ❌ ERROR: Twitter API rate limit exceeded. Try increasing the delay between posts.")
        return False
    except Exception as e:
        print(f"   ❌ AN UNEXPECTED ERROR OCCURRED while posting to X: {e}")
        return False
    finally:
        # Clean up the downloaded image
        if os.path.exists(local_image_path):
            os.remove(local_image_path)