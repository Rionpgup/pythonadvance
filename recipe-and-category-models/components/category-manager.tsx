"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Badge } from "@/components/ui/badge"
import { Plus, Pencil, Trash2, FolderOpen } from "lucide-react"

interface Category {
  id: number
  name: string
}

export function CategoryManager() {
  const [categories, setCategories] = useState<Category[]>([
    { id: 1, name: "Italian" },
    { id: 2, name: "Mexican" },
    { id: 3, name: "Asian" },
  ])
  const [newCategoryName, setNewCategoryName] = useState("")
  const [editingId, setEditingId] = useState<number | null>(null)
  const [editName, setEditName] = useState("")

  const handleCreate = () => {
    if (newCategoryName.trim()) {
      const newCategory: Category = {
        id: Math.max(0, ...categories.map((c) => c.id)) + 1,
        name: newCategoryName.trim(),
      }
      setCategories([...categories, newCategory])
      setNewCategoryName("")
    }
  }

  const handleUpdate = (id: number) => {
    if (editName.trim()) {
      setCategories(categories.map((c) => (c.id === id ? { ...c, name: editName.trim() } : c)))
      setEditingId(null)
      setEditName("")
    }
  }

  const handleDelete = (id: number) => {
    setCategories(categories.filter((c) => c.id !== id))
  }

  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <Card className="border-border">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Plus className="h-5 w-5 text-primary" />
            Create Category
          </CardTitle>
          <CardDescription>Add a new category to organize your recipes</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="category-name">Category Name</Label>
            <Input
              id="category-name"
              placeholder="e.g., Italian, Mexican, Asian..."
              value={newCategoryName}
              onChange={(e) => setNewCategoryName(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleCreate()}
            />
          </div>
          <Button onClick={handleCreate} className="w-full">
            <Plus className="mr-2 h-4 w-4" />
            Create Category
          </Button>

          <div className="pt-4 border-t border-border">
            <h3 className="text-sm font-medium text-muted-foreground mb-3">Model: CategoryCreate</h3>
            <div className="rounded-lg bg-muted/50 p-3 font-mono text-xs">
              <div className="text-primary">class CategoryCreate:</div>
              <div className="ml-4 text-foreground">name: str</div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card className="border-border">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <FolderOpen className="h-5 w-5 text-primary" />
            All Categories
          </CardTitle>
          <CardDescription>
            {categories.length} {categories.length === 1 ? "category" : "categories"} in the database
          </CardDescription>
        </CardHeader>
        <CardContent>
          {categories.length === 0 ? (
            <div className="text-center py-8 text-muted-foreground">No categories yet. Create your first one!</div>
          ) : (
            <div className="space-y-2">
              {categories.map((category) => (
                <div
                  key={category.id}
                  className="flex items-center justify-between p-3 rounded-lg bg-card border border-border hover:border-primary/50 transition-colors"
                >
                  {editingId === category.id ? (
                    <Input
                      value={editName}
                      onChange={(e) => setEditName(e.target.value)}
                      onKeyDown={(e) => e.key === "Enter" && handleUpdate(category.id)}
                      className="flex-1 mr-2"
                      autoFocus
                    />
                  ) : (
                    <div className="flex items-center gap-3 flex-1">
                      <Badge variant="outline" className="font-mono text-xs">
                        ID: {category.id}
                      </Badge>
                      <span className="font-medium text-foreground">{category.name}</span>
                    </div>
                  )}
                  <div className="flex gap-2">
                    {editingId === category.id ? (
                      <>
                        <Button size="sm" variant="outline" onClick={() => handleUpdate(category.id)}>
                          Save
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => {
                            setEditingId(null)
                            setEditName("")
                          }}
                        >
                          Cancel
                        </Button>
                      </>
                    ) : (
                      <>
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => {
                            setEditingId(category.id)
                            setEditName(category.name)
                          }}
                        >
                          <Pencil className="h-4 w-4" />
                        </Button>
                        <Button
                          size="sm"
                          variant="ghost"
                          onClick={() => handleDelete(category.id)}
                          className="text-destructive hover:text-destructive"
                        >
                          <Trash2 className="h-4 w-4" />
                        </Button>
                      </>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}
