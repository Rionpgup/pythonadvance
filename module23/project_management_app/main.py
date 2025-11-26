from fastapi import FastAPI
from models import Developer, Project

app = FastAPI()

@app.post("/developers/")   # new *
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}

@app.post("/projects/")    # new *
def create_project(project: Project):
    return {"message": "Project created successfully", "project": project}

@app.get("/projects/")    # new *
def get_projects():
    sample_project = Project(
        title="Sample Project",
        description="This is aSample Description",
        languages=["Python", "JavaScript"],
        lead_developer=Developer(name="Jane Doe", expereience=5)
    )
    return {"projects": [sample_project]}