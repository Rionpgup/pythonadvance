"use client"

import { useState } from "react"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { CategoryManager } from "@/components/category-manager"
import { RecipeManager } from "@/components/recipe-manager"
import { ApiDocumentation } from "@/components/api-documentation"
import { ChefHat, Database, FileCode } from "lucide-react"

export default function RecipeManagementDashboard() {
  const [activeTab, setActiveTab] = useState("categories")

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary">
              <ChefHat className="h-6 w-6 text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-foreground">Recipe Management API</h1>
              <p className="text-sm text-muted-foreground">Category & Recipe Models Dashboard</p>
            </div>
          </div>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h2 className="text-3xl font-bold text-foreground mb-2">API Dashboard</h2>
          <p className="text-muted-foreground">
            Manage categories and recipes with full CRUD operations using Python models and routers
          </p>
        </div>

        <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
          <TabsList className="grid w-full grid-cols-3 lg:w-auto lg:inline-grid">
            <TabsTrigger value="categories" className="gap-2">
              <Database className="h-4 w-4" />
              Categories
            </TabsTrigger>
            <TabsTrigger value="recipes" className="gap-2">
              <ChefHat className="h-4 w-4" />
              Recipes
            </TabsTrigger>
            <TabsTrigger value="documentation" className="gap-2">
              <FileCode className="h-4 w-4" />
              API Docs
            </TabsTrigger>
          </TabsList>

          <TabsContent value="categories" className="space-y-6">
            <CategoryManager />
          </TabsContent>

          <TabsContent value="recipes" className="space-y-6">
            <RecipeManager />
          </TabsContent>

          <TabsContent value="documentation" className="space-y-6">
            <ApiDocumentation />
          </TabsContent>
        </Tabs>
      </main>
    </div>
  )
}
