def get_search_theme() -> str:
    """
    Prompts the user to enter a search theme and ensures it's not empty.
    """
    while True:
        theme = input("▶️ Enter the general search theme (e.g., 'pink setup', 'kitchen tools'): ")
        if theme.strip():  # .strip() removes whitespace from the beginning and end
            return theme
        else:
            print("❌ The theme cannot be empty. Please try again.")

def get_post_quantity() -> int:
    """
    Prompts the user for the number of posts to publish and validates the input.
    """
    while True:
        quantity_str = input("▶️ How many posts would you like to publish? ")
        try:
            quantity = int(quantity_str)
            if quantity > 0:
                return quantity
            else:
                print("❌ Please enter a positive number (1 or more).")
        except ValueError:
            print("❌ Invalid input. Please enter a whole number.")