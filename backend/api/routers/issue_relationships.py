from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Issue Relationships CRUD endpoints
# ==============================================================================


@router.post("/issue/{issue_id}/relationship")
async def create_issue_relationship(issue_id: int):
    return {"message": f"Create issue relationship for issue {issue_id}"}


@router.get("/issue/{issue_id}/relationship")
async def get_issue_relationship(issue_id: int):
    return {"message": f"Get issue relationship for issue {issue_id}"}


@router.put("/issue/{issue_id}/relationship")
async def update_issue_relationship(issue_id: int):
    return {"message": f"Update issue relationship for issue {issue_id}"}


@router.delete("/issue/{issue_id}/relationship")
async def delete_issue_relationship(issue_id: int):
    return {"message": f"Delete issue relationship for issue {issue_id}"}
