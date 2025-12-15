from pydantic import BaseModel, Field
from typing import Optional


# Category Models
class CategoryBase(BaseModel):
    """Base model containing only the name field."""
    name: str = Field(..., min_length=1, max_length=100, description="The name of the category")


class CategoryCreate(CategoryBase):
    """Used for creating new categories. Inherits all attributes from CategoryBase."""
    pass


class CategoryResponse(BaseModel):
    """Returned when querying a category, including id and name."""
    id: int = Field(..., description="The unique identifier of the category")
    name: str = Field(..., description="The name of the category")

    class Config:
        from_attributes = True


class Category(BaseModel):
    """Represents a full category object with id and name."""
    id: int = Field(..., description="The unique identifier of the category")
    name: str = Field(..., description="The name of the category")

    class Config:
        from_attributes = True


# Recipe Models
class RecipeBase(BaseModel):
    """Base model for recipes, containing all required fields and optional fields."""
    name: str = Field(..., min_length=1, max_length=200, description="The name of the recipe")
    description: Optional[str] = Field(None, description="A brief description of the recipe, optional")
    ingredients: str = Field(..., description="The ingredients required for the recipe")
    instructions: str = Field(..., description="The steps to prepare the recipe")
    cuisine: str = Field(..., min_length=1, max_length=50, description="The type of cuisine the recipe belongs to")
    difficulty: str = Field(..., min_length=1, max_length=20, description="The level of difficulty to prepare the recipe")
    category_id: Optional[int] = Field(None, description="The ID of the category the recipe belongs to, optional")


class RecipeCreate(RecipeBase):
    """Used when creating a new recipe, includes all fields from RecipeBase."""
    pass


class Recipe(RecipeBase):
    """Represents a full recipe object with an 'id' and all other attributes."""
    id: int = Field(..., description="The unique identifier of the recipe")

    class Config:
        from_attributes = True
