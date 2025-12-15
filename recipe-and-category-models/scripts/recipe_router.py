from typing import List, Optional
from models import Recipe, RecipeCreate
from database import (
    get_all_recipes,
    create_recipe_db,
    update_recipe_db,
    delete_recipe_db,
    category_exists as db_category_exists
)


def get_recipes(cuisine: str = None, difficulty: str = None) -> List[Recipe]:
    """
    Retrieves recipes from the database with optional filters for cuisine and difficulty.
    
    Parameters:
        cuisine: str = None - Filter recipes by cuisine.
        difficulty: str = None - Filter recipes by difficulty.
    
    Returns:
        List[Recipe]: A list of Recipe objects matching the specified filters.
    """
    return get_all_recipes(cuisine=cuisine, difficulty=difficulty)


def create_recipe(recipe: RecipeCreate) -> Recipe:
    """
    Creates a new recipe in the database.
    
    Parameters:
        recipe: RecipeCreate - The recipe data to be created.
    
    Returns:
        Recipe: The created Recipe object with its generated ID.
    
    Raises:
        ValueError: If the category_id is provided but does not exist in the database.
    """
    # Validate category exists if category_id is provided
    if recipe.category_id is not None:
        if not db_category_exists(recipe.category_id):
            raise ValueError(f"Category with ID {recipe.category_id} does not exist")
    
    return create_recipe_db(recipe)


def update_recipe(recipe_id: int, recipe: RecipeCreate) -> Recipe:
    """
    Updates an existing recipe in the database.
    
    Parameters:
        recipe_id: int - The ID of the recipe to be updated.
        recipe: RecipeCreate - The new data for the recipe.
    
    Returns:
        Recipe: The updated Recipe object.
    
    Raises:
        ValueError: If the recipe or category does not exist.
    """
    # Validate category exists if category_id is provided
    if recipe.category_id is not None:
        if not db_category_exists(recipe.category_id):
            raise ValueError(f"Category with ID {recipe.category_id} does not exist")
    
    updated_recipe = update_recipe_db(recipe_id, recipe)
    if updated_recipe is None:
        raise ValueError(f"Recipe with ID {recipe_id} not found")
    return updated_recipe


def delete_recipe(recipe_id: int) -> dict:
    """
    Deletes a recipe from the database by ID.
    
    Parameters:
        recipe_id: int - The ID of the recipe to be deleted.
    
    Returns:
        dict: A dictionary with a detail message indicating the recipe has been deleted.
    
    Raises:
        ValueError: If the recipe with the given ID does not exist.
    """
    if delete_recipe_db(recipe_id):
        return {"detail": f"Recipe with ID {recipe_id} has been deleted"}
    else:
        raise ValueError(f"Recipe with ID {recipe_id} not found")


def category_exists(category_id: int) -> bool:
    """
    Checks if a category with the given ID exists in the database (helper function).
    
    Parameters:
        category_id: int - The ID of the category to check.
    
    Returns:
        bool: True if the category exists, False otherwise.
    """
    return db_category_exists(category_id)
