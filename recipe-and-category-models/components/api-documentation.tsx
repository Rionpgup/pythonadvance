"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"

export function ApiDocumentation() {
  return (
    <div className="space-y-6">
      <Tabs defaultValue="models" className="space-y-6">
        <TabsList>
          <TabsTrigger value="models">Models</TabsTrigger>
          <TabsTrigger value="category-router">Category Router</TabsTrigger>
          <TabsTrigger value="recipe-router">Recipe Router</TabsTrigger>
        </TabsList>

        <TabsContent value="models" className="space-y-6">
          <Card className="border-border bg-primary/5">
            <CardHeader>
              <CardTitle className="text-2xl">Category Models</CardTitle>
              <CardDescription>
                The category models define the structure for managing categories, which are used to group recipes.
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="space-y-4">
                <ModelCard
                  name="CategoryBase"
                  purpose="Base model, containing only the name field."
                  attributes={["name (str): The name of the category"]}
                />
                <ModelCard
                  name="CategoryCreate"
                  purpose="Used for creating new categories."
                  attributes={["Inherits all attributes from 'CategoryBase'."]}
                />
                <ModelCard
                  name="CategoryResponse"
                  purpose="Returned when querying a category, including id and name."
                  attributes={["id", "name"]}
                />
                <ModelCard
                  name="Category"
                  purpose="Represents a full category object with id and name."
                  attributes={["id", "Inherits 'name' from CategoryBase."]}
                />
              </div>
            </CardContent>
          </Card>

          <Card className="border-border bg-primary/5">
            <CardHeader>
              <CardTitle className="text-2xl">Recipe Models</CardTitle>
              <CardDescription>The recipe models define the structure for managing recipes.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              <div className="space-y-4">
                <ModelCard
                  name="RecipeBase"
                  purpose="Serves as the base model for recipes, containing all required fields and optional fields like 'description' and 'category_id'."
                  attributes={[
                    "name (str): The name of the recipe.",
                    "description (Optional[str]): A brief description of the recipe, optional.",
                    "ingredients (str): The ingredients required for the recipe.",
                    "instructions (str): The steps to prepare the recipe.",
                    "cuisine (str): The type of cuisine the recipe belongs to.",
                    "difficulty (str): The level of difficulty to prepare the recipe.",
                    "category_id (Optional[int]): The ID of the category the recipe belongs to, optional.",
                  ]}
                />
                <ModelCard
                  name="RecipeCreate"
                  purpose="Used when creating a new recipe, as it includes all fields from 'RecipeBase'."
                  attributes={["Inherits all attributes from 'RecipeBase'."]}
                />
                <ModelCard
                  name="Recipe"
                  purpose="Represents a full recipe object with an 'id' and all other attributes, typically used for operations involving existing recipes."
                  attributes={[
                    "id (int): The unique identifier of the recipe.",
                    "Inherits all fields from 'RecipeBase'.",
                  ]}
                />
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="category-router" className="space-y-6">
          <Card className="border-border">
            <CardHeader>
              <CardTitle className="text-2xl">Category Router</CardTitle>
              <CardDescription>API endpoints for managing categories</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <RouterFunction
                name="get_categories"
                method="GET"
                description="Retrieves all categories from the database."
                parameters="None"
                returns="List[Category]: A list of Category objects representing all categories in the database."
              />
              <RouterFunction
                name="create_category"
                method="POST"
                description="Creates a new category in the database."
                parameters="category: CategoryCreate - The category data to be created."
                returns="Category: The created Category object with its generated ID."
              />
              <RouterFunction
                name="update_category"
                method="PUT"
                description="Updates the name of an existing category by its ID."
                parameters="category_id: int - The ID of the category to be updated. category: CategoryCreate - The new data for the category."
                returns="Category: The updated Category object."
              />
              <RouterFunction
                name="delete_category"
                method="DELETE"
                description="Deletes a category from the database by its ID."
                parameters="category_id: int - The ID of the category to be deleted."
                returns="dict: A dictionary with a detail message indicating the category has been deleted."
              />
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="recipe-router" className="space-y-6">
          <Card className="border-border">
            <CardHeader>
              <CardTitle className="text-2xl">Recipe Router</CardTitle>
              <CardDescription>API endpoints for managing recipes</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <RouterFunction
                name="get_recipes"
                method="GET"
                description="Retrieves recipes from the database with optional filters for cuisine and difficulty."
                parameters="cuisine: str = None - Filter recipes by cuisine. difficulty: str = None - Filter recipes by difficulty."
                returns="List[Recipe]: A list of Recipe objects matching the specified filters."
              />
              <RouterFunction
                name="create_recipe"
                method="POST"
                description="Creates a new recipe in the database."
                parameters="recipe: RecipeCreate - The recipe data to be created."
                returns="Recipe: The created Recipe object with its generated ID."
              />
              <RouterFunction
                name="update_recipe"
                method="PUT"
                description="Updates an existing recipe in the database."
                parameters="recipe_id: int - The ID of the recipe to be updated. recipe: RecipeCreate - The new data for the recipe."
                returns="Recipe: The updated Recipe object."
              />
              <RouterFunction
                name="delete_recipe"
                method="DELETE"
                description="Deletes a recipe from the database by ID."
                parameters="recipe_id: int - The ID of the recipe to be deleted."
                returns="dict: A dictionary with a detail message indicating the recipe has been deleted."
              />
              <RouterFunction
                name="category_exists"
                method="HELPER"
                description="Checks if a category with the given ID exists in the database. (helper function)"
                parameters="category_id: int - The ID of the category to check."
                returns="bool: True if the category exists, False otherwise."
              />
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  )
}

function ModelCard({
  name,
  purpose,
  attributes,
}: {
  name: string
  purpose: string
  attributes: string[]
}) {
  return (
    <Card className="border-border bg-card">
      <CardHeader>
        <CardTitle className="text-lg flex items-center gap-2">
          <Badge className="font-mono">{name}</Badge>
        </CardTitle>
        <CardDescription>{purpose}</CardDescription>
      </CardHeader>
      <CardContent>
        <div className="space-y-2">
          <p className="text-sm font-medium text-foreground">Attributes:</p>
          <ul className="space-y-1">
            {attributes.map((attr, index) => (
              <li key={index} className="text-sm text-muted-foreground pl-4 border-l-2 border-primary/30">
                {attr}
              </li>
            ))}
          </ul>
        </div>
      </CardContent>
    </Card>
  )
}

function RouterFunction({
  name,
  method,
  description,
  parameters,
  returns,
}: {
  name: string
  method: string
  description: string
  parameters: string
  returns: string
}) {
  const methodColors = {
    GET: "bg-blue-500/10 text-blue-500",
    POST: "bg-emerald-500/10 text-emerald-500",
    PUT: "bg-amber-500/10 text-amber-500",
    DELETE: "bg-red-500/10 text-red-500",
    HELPER: "bg-purple-500/10 text-purple-500",
  }

  return (
    <Card className="border-border bg-card">
      <CardHeader>
        <div className="flex items-center gap-2 mb-2">
          <Badge className={methodColors[method as keyof typeof methodColors]}>{method}</Badge>
          <code className="font-mono text-sm text-foreground">{name}</code>
        </div>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent className="space-y-3">
        <div>
          <p className="text-sm font-medium text-foreground mb-1">Parameters:</p>
          <p className="text-sm text-muted-foreground pl-4 border-l-2 border-primary/30">{parameters}</p>
        </div>
        <div>
          <p className="text-sm font-medium text-foreground mb-1">Returns:</p>
          <p className="text-sm text-muted-foreground pl-4 border-l-2 border-primary/30">{returns}</p>
        </div>
      </CardContent>
    </Card>
  )
}
