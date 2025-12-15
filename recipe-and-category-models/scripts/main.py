"""
Recipe Management System
========================

This is a complete recipe and category management system demonstrating
all the models and router functions specified in your requirements.

Usage:
    Run this script to see examples of all CRUD operations for both
    categories and recipes.
"""

from models import CategoryCreate, RecipeCreate
from category_router import (
    get_categories,
    create_category,
    update_category,
    delete_category
)
from recipe_router import (
    get_recipes,
    create_recipe,
    update_recipe,
    delete_recipe,
    category_exists
)


def print_separator(title: str = ""):
    """Print a visual separator for better output readability."""
    print("\n" + "=" * 60)
    if title:
        print(f" {title}")
        print("=" * 60)


def demonstrate_category_operations():
    """Demonstrate all category CRUD operations."""
    print_separator("CATEGORY OPERATIONS")
    
    # Create categories
    print("\n1. Creating categories...")
    italian = create_category(CategoryCreate(name="Italian"))
    print(f"   Created: {italian.name} (ID: {italian.id})")
    
    mexican = create_category(CategoryCreate(name="Mexican"))
    print(f"   Created: {mexican.name} (ID: {mexican.id})")
    
    asian = create_category(CategoryCreate(name="Asian"))
    print(f"   Created: {asian.name} (ID: {asian.id})")
    
    # Get all categories
    print("\n2. Retrieving all categories...")
    all_categories = get_categories()
    for cat in all_categories:
        print(f"   - {cat.name} (ID: {cat.id})")
    
    # Update a category
    print("\n3. Updating a category...")
    updated = update_category(2, CategoryCreate(name="Mexican Cuisine"))
    print(f"   Updated category ID 2 to: {updated.name}")
    
    # Get all categories again
    print("\n4. Retrieving all categories after update...")
    all_categories = get_categories()
    for cat in all_categories:
        print(f"   - {cat.name} (ID: {cat.id})")
    
    # Delete a category
    print("\n5. Deleting a category...")
    result = delete_category(3)
    print(f"   {result['detail']}")
    
    # Final category list
    print("\n6. Final category list...")
    all_categories = get_categories()
    for cat in all_categories:
        print(f"   - {cat.name} (ID: {cat.id})")
    
    return italian.id, mexican.id


def demonstrate_recipe_operations(italian_id: int, mexican_id: int):
    """Demonstrate all recipe CRUD operations."""
    print_separator("RECIPE OPERATIONS")
    
    # Create recipes
    print("\n1. Creating recipes...")
    
    pasta = create_recipe(RecipeCreate(
        name="Spaghetti Carbonara",
        description="Classic Italian pasta dish",
        ingredients="Spaghetti, eggs, pancetta, parmesan, black pepper",
        instructions="1. Cook pasta. 2. Fry pancetta. 3. Mix eggs and cheese. 4. Combine all.",
        cuisine="Italian",
        difficulty="Medium",
        category_id=italian_id
    ))
    print(f"   Created: {pasta.name} (ID: {pasta.id})")
    
    tacos = create_recipe(RecipeCreate(
        name="Beef Tacos",
        description="Delicious Mexican tacos",
        ingredients="Ground beef, taco shells, lettuce, cheese, salsa",
        instructions="1. Cook beef. 2. Warm shells. 3. Assemble tacos.",
        cuisine="Mexican",
        difficulty="Easy",
        category_id=mexican_id
    ))
    print(f"   Created: {tacos.name} (ID: {tacos.id})")
    
    pizza = create_recipe(RecipeCreate(
        name="Margherita Pizza",
        description="Simple and classic pizza",
        ingredients="Pizza dough, tomato sauce, mozzarella, basil",
        instructions="1. Roll dough. 2. Add sauce. 3. Add toppings. 4. Bake at 450°F.",
        cuisine="Italian",
        difficulty="Hard",
        category_id=italian_id
    ))
    print(f"   Created: {pizza.name} (ID: {pizza.id})")
    
    # Get all recipes
    print("\n2. Retrieving all recipes...")
    all_recipes = get_recipes()
    for recipe in all_recipes:
        print(f"   - {recipe.name} (Cuisine: {recipe.cuisine}, Difficulty: {recipe.difficulty})")
    
    # Filter by cuisine
    print("\n3. Filtering recipes by cuisine (Italian)...")
    italian_recipes = get_recipes(cuisine="Italian")
    for recipe in italian_recipes:
        print(f"   - {recipe.name}")
    
    # Filter by difficulty
    print("\n4. Filtering recipes by difficulty (Easy)...")
    easy_recipes = get_recipes(difficulty="Easy")
    for recipe in easy_recipes:
        print(f"   - {recipe.name}")
    
    # Check if category exists
    print("\n5. Checking if category exists...")
    exists = category_exists(italian_id)
    print(f"   Category {italian_id} exists: {exists}")
    exists = category_exists(999)
    print(f"   Category 999 exists: {exists}")
    
    # Update a recipe
    print("\n6. Updating a recipe...")
    updated_recipe = update_recipe(1, RecipeCreate(
        name="Authentic Spaghetti Carbonara",
        description="Traditional Italian pasta dish from Rome",
        ingredients="Spaghetti, eggs, guanciale, pecorino romano, black pepper",
        instructions="1. Cook pasta al dente. 2. Fry guanciale. 3. Mix eggs and cheese. 4. Combine off heat.",
        cuisine="Italian",
        difficulty="Hard",
        category_id=italian_id
    ))
    print(f"   Updated: {updated_recipe.name} (Difficulty: {updated_recipe.difficulty})")
    
    # Get all recipes after update
    print("\n7. Retrieving all recipes after update...")
    all_recipes = get_recipes()
    for recipe in all_recipes:
        print(f"   - {recipe.name} (Difficulty: {recipe.difficulty})")
    
    # Delete a recipe
    print("\n8. Deleting a recipe...")
    result = delete_recipe(2)
    print(f"   {result['detail']}")
    
    # Final recipe list
    print("\n9. Final recipe list...")
    all_recipes = get_recipes()
    for recipe in all_recipes:
        print(f"   - {recipe.name}")


def main():
    """Main function to run all demonstrations."""
    print_separator("RECIPE MANAGEMENT SYSTEM DEMO")
    print("\nThis demo showcases all the models and router functions")
    print("for managing categories and recipes.")
    
    # Demonstrate category operations
    italian_id, mexican_id = demonstrate_category_operations()
    
    # Demonstrate recipe operations
    demonstrate_recipe_operations(italian_id, mexican_id)
    
    print_separator("DEMO COMPLETE")
    print("\nAll operations completed successfully!")
    print("You can now use these functions in your PyCharm project.\n")


if __name__ == "__main__":
    main()
