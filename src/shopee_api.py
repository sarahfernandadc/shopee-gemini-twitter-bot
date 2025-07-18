import time
import hashlib
import json
import requests

class ShopeeClient:
    """
    A client to interact with the Shopee Affiliate Open API.
    Handles request signing and data fetching for products.
    """
    def __init__(self, app_id: str, secret_key: str):
        """Initializes the ShopeeClient."""
        self.app_id = app_id
        self.secret_key = secret_key
        self.api_url = "https://open-api.affiliate.shopee.com.br/graphql"
        if not self.app_id or not self.secret_key:
            raise ValueError("Shopee App ID and Secret Key cannot be empty.")

    def _generate_signature(self, payload: str, timestamp: int) -> str:
        """Generates the required SHA256 signature for API requests."""
        base_string = f"{self.app_id}{timestamp}{payload}{self.secret_key}"
        return hashlib.sha256(base_string.encode('utf-8')).hexdigest()

    def search_products(self, keyword: str, limit: int = 1, sort_type: int = 2) -> list:
        """
        Searches for products on Shopee based on a keyword.

        Args:
            keyword: The search term for products.
            limit: The maximum number of products to return.
            sort_type: The sorting method (2=Relevance, 4=Top Sales).

        Returns:
            A list of product dictionaries, or an empty list if none are found or an error occurs.
        """
        print(f"\n🔍 Searching Shopee for '{keyword}'...")

        query = f"""
        {{
            productOfferV2(keyword: "{keyword}", limit: {limit}, sortType: {sort_type}) {{
                nodes {{
                    productName
                    imageUrl
                    priceMin
                    priceMax
                    shopName
                    productLink
                    commissionRate
                    offerLink
                }}
            }}
        }}
        """
        payload = json.dumps({"query": query})
        timestamp = int(time.time())
        signature = self._generate_signature(payload, timestamp)

        headers = {
            "Authorization": f"SHA256 Credential={self.app_id}, Timestamp={timestamp}, Signature={signature}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(self.api_url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
            data = response.json()

            if "errors" in data and data["errors"]:
                print(f"❌ Shopee API returned an error: {data['errors']}")
                return []

            nodes = data.get("data", {}).get("productOfferV2", {}).get("nodes")
            if not nodes:
                print("   No products found for this keyword.")
                return []

            print(f"   ✅ Found {len(nodes)} product(s).")
            return nodes
        except requests.exceptions.RequestException as e:
            print(f"❌ A connection error occurred while searching for products: {e}")
            return []