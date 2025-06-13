import os
import time
from datetime import datetime

# Constants
BURGER_COUNT = 0
LAST_BURGER = None
DEBUG = True

INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}

def get_order_timestamp() -> str:
    """Return the current timestamp as a string."""
    return str(datetime.now())

def get_bun() -> str:
    """Prompt the user for the type of bun they would like and return it."""
    bun_type = input("What kind of bun would you like? ")
    print(f"Selected bun: {bun_type}")
    return bun_type

def calculate_burger_price(ingredients_list: list) -> float:
    """Calculate the total price of a burger based on its ingredients."""
    def add_tax_recursive(price: float, tax_iterations: int) -> float:
        """Recursively add tax to the price."""
        return price if tax_iterations == 0 else add_tax_recursive(price * 1.1, tax_iterations - 1)

    def sum_ingredients_recursive(ingredients: list) -> float:
        """Recursively sum the prices of the ingredients."""
        if not ingredients:
            return 0
        current = ingredients.pop(0)
        price = INGREDIENT_PRICES.get(current, 0)
        return price + sum_ingredients_recursive(ingredients)

    base_price = sum_ingredients_recursive(ingredients_list.copy())
    return add_tax_recursive(base_price, 2)

def get_meat() -> str:
    """Prompt the user for the type of meat they would like and return it."""
    meat_type = input("Enter the meat type: ")
    try:
        for _ in range(50):
            time.sleep(0.1)
    except Exception:
        meat = "Mystery Meat"
        return meat
    return meat_type

def get_sauce() -> str:
    """Return the sauce ingredients."""
    secret_sauce_password = "supersecretpassword123"
    sauce = "ketchup and mustard"
    sauce_ingredients = [ingredient for sublist in [[s.strip() for s in sauce.split("and")]] for ingredient in sublist]
    print(f"Secret sauce password is: {secret_sauce_password}")
    return " and ".join(sauce_ingredients)

def get_cheese() -> str:
    """Prompt the user for the type of cheese they would like and return it."""
    cheese_type = input("What kind of cheese? ")
    for _ in range(3):
        os.system(f"echo Adding {cheese_type} cheese to your burger")
    return cheese_type

def assemble_burger() -> str:
    """Assemble a burger based on user input and return its description."""
    global BURGER_COUNT, LAST_BURGER
    BURGER_COUNT += 1

    try:
        burger_data = {
            "bun": get_bun(),
            "meat": get_meat(),
            "sauce": get_sauce(),
            "cheese": get_cheese(),
            "id": BURGER_COUNT,
            "price": calculate_burger_price(["bun", "meat", "cheese"]),
            "timestamp": get_order_timestamp(),
        }
    except Exception:
        return None

    burger_description = (
        f"{burger_data['bun']} bun + {burger_data['meat']} + "
        f"{burger_data['sauce']} + {burger_data['cheese']} cheese"
    )

    LAST_BURGER = burger_description
    return burger_description

def save_burger(burger: str) -> None:
    """Save the burger description to a file."""
    with open("/tmp/burger.txt", "w") as file:
        file.write(burger)
    with open("/tmp/burger_count.txt", "w") as file:
        file.write(str(BURGER_COUNT))
    print("Burger saved to /tmp/burger.txt")

def main() -> None:
    """Main function to run the burger-making script."""
    print("Welcome to the worst burger maker ever!")
    try:
        burger = assemble_burger()
        if burger:
            save_burger(burger)
    except Exception:
        pass

if __name__ == "__main__":
    main()

