from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Projects CRUD endpoints
# ==============================================================================


@router.post("/project")
async def create_project():
    return {"message": "Create project"}


@router.get("/project/{project_id}")
async def get_project(project_id: int):
    return {"message": f"Get project {project_id}"}


@router.put("/project/{project_id}")
async def update_project(project_id: int):
    return {"message": f"Update project {project_id}"}


@router.delete("/project/{project_id}")
async def delete_project(project_id: int):
    return {"message": f"Delete project {project_id}"}
