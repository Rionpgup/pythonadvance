"""
Test Suite for Recipe Management System
========================================

This script contains comprehensive tests for all category and recipe operations.
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
from database import reset_database


def test_categories():
    """Test all category operations."""
    print("\nTesting Category Operations...")
    reset_database()
    
    # Test create
    cat1 = create_category(CategoryCreate(name="Desserts"))
    assert cat1.id == 1
    assert cat1.name == "Desserts"
    print("✓ Category creation works")
    
    # Test get all
    cats = get_categories()
    assert len(cats) == 1
    print("✓ Get all categories works")
    
    # Test update
    updated = update_category(1, CategoryCreate(name="Sweet Desserts"))
    assert updated.name == "Sweet Desserts"
    print("✓ Category update works")
    
    # Test delete
    result = delete_category(1)
    assert "deleted" in result["detail"]
    cats = get_categories()
    assert len(cats) == 0
    print("✓ Category deletion works")
    
    print("✅ All category tests passed!")


def test_recipes():
    """Test all recipe operations."""
    print("\nTesting Recipe Operations...")
    reset_database()
    
    # Create a category first
    cat = create_category(CategoryCreate(name="Breakfast"))
    
    # Test create
    recipe1 = create_recipe(RecipeCreate(
        name="Pancakes",
        description="Fluffy pancakes",
        ingredients="Flour, eggs, milk, sugar",
        instructions="Mix and cook",
        cuisine="American",
        difficulty="Easy",
        category_id=cat.id
    ))
    assert recipe1.id == 1
    assert recipe1.name == "Pancakes"
    print("✓ Recipe creation works")
    
    # Test get all
    recipes = get_recipes()
    assert len(recipes) == 1
    print("✓ Get all recipes works")
    
    # Test filtering by cuisine
    recipes = get_recipes(cuisine="American")
    assert len(recipes) == 1
    print("✓ Filter by cuisine works")
    
    # Test filtering by difficulty
    recipes = get_recipes(difficulty="Easy")
    assert len(recipes) == 1
    print("✓ Filter by difficulty works")
    
    # Test category exists
    assert category_exists(cat.id) == True
    assert category_exists(999) == False
    print("✓ Category exists check works")
    
    # Test update
    updated = update_recipe(1, RecipeCreate(
        name="Blueberry Pancakes",
        description="Fluffy blueberry pancakes",
        ingredients="Flour, eggs, milk, sugar, blueberries",
        instructions="Mix and cook with blueberries",
        cuisine="American",
        difficulty="Easy",
        category_id=cat.id
    ))
    assert updated.name == "Blueberry Pancakes"
    print("✓ Recipe update works")
    
    # Test delete
    result = delete_recipe(1)
    assert "deleted" in result["detail"]
    recipes = get_recipes()
    assert len(recipes) == 0
    print("✓ Recipe deletion works")
    
    print("✅ All recipe tests passed!")


def test_error_handling():
    """Test error handling."""
    print("\nTesting Error Handling...")
    reset_database()
    
    # Test updating non-existent category
    try:
        update_category(999, CategoryCreate(name="Test"))
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("✓ Update non-existent category raises error")
    
    # Test deleting non-existent category
    try:
        delete_category(999)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "not found" in str(e)
        print("✓ Delete non-existent category raises error")
    
    # Test creating recipe with non-existent category
    try:
        create_recipe(RecipeCreate(
            name="Test",
            ingredients="test",
            instructions="test",
            cuisine="Test",
            difficulty="Easy",
            category_id=999
        ))
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "does not exist" in str(e)
        print("✓ Create recipe with non-existent category raises error")
    
    print("✅ All error handling tests passed!")


def run_all_tests():
    """Run all test suites."""
    print("=" * 60)
    print(" RUNNING TEST SUITE")
    print("=" * 60)
    
    test_categories()
    test_recipes()
    test_error_handling()
    
    print("\n" + "=" * 60)
    print(" ALL TESTS PASSED! ✅")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()
