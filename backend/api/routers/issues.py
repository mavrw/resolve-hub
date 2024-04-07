from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Issues CRUD endpoints
# ==============================================================================


@router.post("/issue")
async def create_issue():
    return {"message": "Create issue"}


@router.get("/issue/{issue_id}")
async def get_issue(issue_id: int):
    return {"message": f"Get issue {issue_id}"}


@router.put("/issue/{issue_id}")
async def update_issue(issue_id: int):
    return {"message": f"Update issue {issue_id}"}


@router.delete("/issue/{issue_id}")
async def delete_issue(issue_id: int):
    return {"message": f"Delete issue {issue_id}"}
