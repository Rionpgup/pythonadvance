from typing import List
from models import Category, CategoryCreate, CategoryResponse
from database import (
    get_all_categories,
    create_category_db,
    update_category_db,
    delete_category_db
)


def get_categories() -> List[Category]:
    """
    Retrieves all categories from the database.
    
    Returns:
        List[Category]: A list of Category objects representing all categories in the database.
    """
    return get_all_categories()


def create_category(category: CategoryCreate) -> Category:
    """
    Creates a new category in the database.
    
    Parameters:
        category: CategoryCreate - The category data to be created.
    
    Returns:
        Category: The created Category object with its generated ID.
    """
    return create_category_db(category)


def update_category(category_id: int, category: CategoryCreate) -> Category:
    """
    Updates the name of an existing category by its ID.
    
    Parameters:
        category_id: int - The ID of the category to be updated.
        category: CategoryCreate - The new data for the category.
    
    Returns:
        Category: The updated Category object.
    
    Raises:
        ValueError: If the category with the given ID does not exist.
    """
    updated_category = update_category_db(category_id, category)
    if updated_category is None:
        raise ValueError(f"Category with ID {category_id} not found")
    return updated_category


def delete_category(category_id: int) -> dict:
    """
    Deletes a category from the database by its ID.
    
    Parameters:
        category_id: int - The ID of the category to be deleted.
    
    Returns:
        dict: A dictionary with a detail message indicating the category has been deleted.
    
    Raises:
        ValueError: If the category with the given ID does not exist.
    """
    if delete_category_db(category_id):
        return {"detail": f"Category with ID {category_id} has been deleted"}
    else:
        raise ValueError(f"Category with ID {category_id} not found")
