class RecipeManager:
    def _init_(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            'ingredients': ingredients,
            'instructions': instructions
        }
        print(f"Recipe '{name}' added.")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes found.")
            return
        for name, details in self.recipes.items():
            print(f"\nRecipe: {name}")
            print("Ingredients:", ", ".join(details['ingredients']))
            print("Instructions:", details['instructions'])

    def delete_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe '{name}' deleted.")
        else:
            print(f"Recipe '{name}' not found.")

def main():
    manager = RecipeManager()

    while True:
        print("\nRecipe Manager")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Delete Recipe")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma separated): ").split(',')
            instructions = input("Enter instructions: ")
            manager.add_recipe(name, [ingredient.strip() for ingredient in ingredients], instructions)

        elif choice == '2':
            manager.view_recipes()

        elif choice == '3':
            name = input("Enter recipe name to delete: ")
            manager.delete_recipe(name)

        elif choice == '4':
            print("Exiting Recipe Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()