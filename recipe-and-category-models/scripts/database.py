from typing import List, Optional, Dict
from models import (
    Category, CategoryCreate, CategoryResponse,
    Recipe, RecipeCreate
)


# In-memory database simulation
categories_db: List[Dict] = []
recipes_db: List[Dict] = []

# Counters for IDs
category_id_counter = 1
recipe_id_counter = 1


def reset_database():
    """Reset the database to empty state."""
    global categories_db, recipes_db, category_id_counter, recipe_id_counter
    categories_db = []
    recipes_db = []
    category_id_counter = 1
    recipe_id_counter = 1


# Category Database Functions
def get_all_categories() -> List[Category]:
    """Retrieves all categories from the database."""
    return [Category(**cat) for cat in categories_db]


def get_category_by_id(category_id: int) -> Optional[Category]:
    """Retrieves a category by its ID."""
    for cat in categories_db:
        if cat['id'] == category_id:
            return Category(**cat)
    return None


def create_category_db(category: CategoryCreate) -> Category:
    """Creates a new category in the database."""
    global category_id_counter
    
    new_category = {
        'id': category_id_counter,
        'name': category.name
    }
    categories_db.append(new_category)
    category_id_counter += 1
    
    return Category(**new_category)


def update_category_db(category_id: int, category: CategoryCreate) -> Optional[Category]:
    """Updates an existing category by its ID."""
    for i, cat in enumerate(categories_db):
        if cat['id'] == category_id:
            categories_db[i]['name'] = category.name
            return Category(**categories_db[i])
    return None


def delete_category_db(category_id: int) -> bool:
    """Deletes a category from the database by its ID."""
    for i, cat in enumerate(categories_db):
        if cat['id'] == category_id:
            categories_db.pop(i)
            return True
    return False


def category_exists(category_id: int) -> bool:
    """Checks if a category with the given ID exists in the database."""
    return any(cat['id'] == category_id for cat in categories_db)


# Recipe Database Functions
def get_all_recipes(cuisine: Optional[str] = None, difficulty: Optional[str] = None) -> List[Recipe]:
    """Retrieves recipes from the database with optional filters for cuisine and difficulty."""
    recipes = [Recipe(**recipe) for recipe in recipes_db]
    
    if cuisine:
        recipes = [r for r in recipes if r.cuisine.lower() == cuisine.lower()]
    
    if difficulty:
        recipes = [r for r in recipes if r.difficulty.lower() == difficulty.lower()]
    
    return recipes


def get_recipe_by_id(recipe_id: int) -> Optional[Recipe]:
    """Retrieves a recipe by its ID."""
    for recipe in recipes_db:
        if recipe['id'] == recipe_id:
            return Recipe(**recipe)
    return None


def create_recipe_db(recipe: RecipeCreate) -> Recipe:
    """Creates a new recipe in the database."""
    global recipe_id_counter
    
    new_recipe = {
        'id': recipe_id_counter,
        'name': recipe.name,
        'description': recipe.description,
        'ingredients': recipe.ingredients,
        'instructions': recipe.instructions,
        'cuisine': recipe.cuisine,
        'difficulty': recipe.difficulty,
        'category_id': recipe.category_id
    }
    recipes_db.append(new_recipe)
    recipe_id_counter += 1
    
    return Recipe(**new_recipe)


def update_recipe_db(recipe_id: int, recipe: RecipeCreate) -> Optional[Recipe]:
    """Updates an existing recipe in the database."""
    for i, rec in enumerate(recipes_db):
        if rec['id'] == recipe_id:
            recipes_db[i] = {
                'id': recipe_id,
                'name': recipe.name,
                'description': recipe.description,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions,
                'cuisine': recipe.cuisine,
                'difficulty': recipe.difficulty,
                'category_id': recipe.category_id
            }
            return Recipe(**recipes_db[i])
    return None


def delete_recipe_db(recipe_id: int) -> bool:
    """Deletes a recipe from the database by ID."""
    for i, rec in enumerate(recipes_db):
        if rec['id'] == recipe_id:
            recipes_db.pop(i)
            return True
    return False
