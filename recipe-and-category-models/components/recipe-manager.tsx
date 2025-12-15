"use client"

import { useState } from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { ChefHat, Filter } from "lu111111111 cide-react"

interface Recipe {
  id: number
  name: string
  description?: string
  ingredients: string
  instructions: string
  cuisine: string
  difficulty: string
  category_id?: number
}

export function RecipeManager() {
  const [recipes, setRecipes] = useState<Recipe[]>([
    {
      id: 1,
      name: "Spaghetti Carbonara",
      description: "Classic Italian pasta dish",
      ingredients: "Pasta, eggs, bacon, parmesan",
      instructions: "Cook pasta, mix with eggs and bacon",
      cuisine: "Italian",
      difficulty: "Medium",
      category_id: 1,
    },
  ])
  const [filterCuisine, setFilterCuisine] = useState<string>("all")
  const [filterDifficulty, setFilterDifficulty] = useState<string>("all")

  const filteredRecipes = recipes.filter((recipe) => {
    const cuisineMatch = filterCuisine === "all" || recipe.cuisine === filterCuisine
    const difficultyMatch = filterDifficulty === "all" || recipe.difficulty === filterDifficulty
    return cuisineMatch && difficultyMatch
  })

  return (
    <div className="space-y-6">
      <Card className="border-border">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Filter className="h-5 w-5 text-primary" />
            Filter Recipes
          </CardTitle>
          <CardDescription>Filter recipes by cuisine and difficulty</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label>Cuisine</Label>
              <Select value={filterCuisine} onValueChange={setFilterCuisine}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Cuisines</SelectItem>
                  <SelectItem value="Italian">Italian</SelectItem>
                  <SelectItem value="Mexican">Mexican</SelectItem>
                  <SelectItem value="Asian">Asian</SelectItem>
                  <SelectItem value="American">American</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label>Difficulty</Label>
              <Select value={filterDifficulty} onValueChange={setFilterDifficulty}>
                <SelectTrigger>
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="all">All Difficulties</SelectItem>
                  <SelectItem value="Easy">Easy</SelectItem>
                  <SelectItem value="Medium">Medium</SelectItem>
                  <SelectItem value="Hard">Hard</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>
        </CardContent>
      </Card>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {filteredRecipes.map((recipe) => (
          <Card key={recipe.id} className="border-border hover:border-primary/50 transition-colors">
            <CardHeader>
              <div className="flex items-start justify-between">
                <ChefHat className="h-5 w-5 text-primary" />
                <Badge variant="outline" className="font-mono text-xs">
                  ID: {recipe.id}
                </Badge>
              </div>
              <CardTitle className="text-lg text-foreground">{recipe.name}</CardTitle>
              {recipe.description && <CardDescription className="text-sm">{recipe.description}</CardDescription>}
            </CardHeader>
            <CardContent className="space-y-3">
              <div className="flex gap-2">
                <Badge className="bg-primary/10 text-primary hover:bg-primary/20">{recipe.cuisine}</Badge>
                <Badge
                  variant="secondary"
                  className={
                    recipe.difficulty === "Easy"
                      ? "bg-emerald-500/10 text-emerald-500"
                      : recipe.difficulty === "Hard"
                        ? "bg-red-500/10 text-red-500"
                        : "bg-amber-500/10 text-amber-500"
                  }
                >
                  {recipe.difficulty}
                </Badge>
              </div>
              <div className="space-y-2 text-sm">
                <div>
                  <span className="font-medium text-foreground">Ingredients:</span>
                  <p className="text-muted-foreground mt-1">{recipe.ingredients}</p>
                </div>
                <div>
                  <span className="font-medium text-foreground">Instructions:</span>
                  <p className="text-muted-foreground mt-1">{recipe.instructions}</p>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {filteredRecipes.length === 0 && (
        <Card className="border-dashed border-border">
          <CardContent className="py-12 text-center">
            <ChefHat className="h-12 w-12 mx-auto mb-4 text-muted-foreground" />
            <p className="text-muted-foreground">No recipes match your filters</p>
          </CardContent>
        </Card>
      )}
    </div>
  )
}
