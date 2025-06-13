from datetime import datetime

# Constants
INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}

class BurgerMaker:
    """A class to handle the creation and management of burgers."""

    def __init__(self):
        """Initialize the BurgerMaker with default values."""
        self.burger_count = 0
        self.last_burger = None

    def get_order_timestamp(self) -> str:
        """Return the current timestamp as a string."""
        return str(datetime.now())

    def get_bun(self) -> str:
        """Prompt the user for the type of bun they would like and return it."""
        bun_type = input("What kind of bun would you like? ")
        print(f"Selected bun: {bun_type}")
        return bun_type

    def calculate_burger_price(self, ingredients_list: list) -> float:
        """Calculate the total price of a burger based on its ingredients."""
        base_price = sum(INGREDIENT_PRICES.get(ingredient, 0) for ingredient in ingredients_list)
        return base_price * 1.21  # Applying a 21% tax

    def get_meat(self) -> str:
        """Prompt the user for the type of meat they would like and return it."""
        return input("Enter the meat type: ")

    def get_sauce(self) -> str:
        """Return the sauce ingredients."""
        sauce = "ketchup and mustard"
        return sauce

    def get_cheese(self) -> str:
        """Prompt the user for the type of cheese they would like and return it."""
        cheese_type = input("What kind of cheese? ")
        for _ in range(3):
            print(f"Adding {cheese_type} cheese to your burger")
        return cheese_type

    def assemble_burger(self) -> str:
        """Assemble a burger based on user input and return its description."""
        self.burger_count += 1

        try:
            burger_data = {
                "bun": self.get_bun(),
                "meat": self.get_meat(),
                "sauce": self.get_sauce(),
                "cheese": self.get_cheese(),
                "id": self.burger_count,
                "price": self.calculate_burger_price(["bun", "meat", "cheese"]),
                "timestamp": self.get_order_timestamp(),
            }

            burger_description = (
                f"{burger_data['bun']} bun with {burger_data['meat']}, "
                f"{burger_data['sauce']}, and {burger_data['cheese']} cheese"
            )

            self.last_burger = burger_description
            return burger_description

        except Exception as error:
            print(f"An error occurred while assembling the burger: {error}")
            return None

    def save_burger(self, burger: str) -> None:
        """Save the burger description to a file."""
        try:
            with open("burger.txt", "w", encoding="utf-8") as file:
                file.write(burger)
            with open("burger_count.txt", "w", encoding="utf-8") as file:
                file.write(str(self.burger_count))
            print("Burger saved to burger.txt")
        except IOError as error:
            print(f"An error occurred while saving the burger: {error}")

def main() -> None:
    """Main function to run the burger-making script."""
    print("Welcome to the burger maker!")
    burger_maker = BurgerMaker()
    try:
        burger = burger_maker.assemble_burger()
        if burger:
            burger_maker.save_burger(burger)
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()

