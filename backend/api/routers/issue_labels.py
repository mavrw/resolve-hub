from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Issue Labels CRUD endpoints
# ==============================================================================


@router.post("/issue/{issue_id}/label")
async def create_issue_label(issue_id: int):
    return {"message": f"Create issue label for issue {issue_id}"}


@router.get("/issue/{issue_id}/label")
async def get_issue_label(issue_id: int):
    return {"message": f"Get issue label for issue {issue_id}"}


@router.put("/issue/{issue_id}/label")
async def update_issue_label(issue_id: int):
    return {"message": f"Update issue label for issue {issue_id}"}


@router.delete("/issue/{issue_id}/label")
async def delete_issue_label(issue_id: int):
    return {"message": f"Delete issue label for issue {issue_id}"}
