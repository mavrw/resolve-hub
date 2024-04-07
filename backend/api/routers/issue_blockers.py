from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Issue Blockers CRUD endpoints
# ==============================================================================


@router.post("/issue/{issue_id}/blocker")
async def create_issue_blocker(issue_id: int):
    return {"message": f"Create issue blocker for issue {issue_id}"}


@router.get("/issue/{issue_id}/blocker")
async def get_issue_blocker(issue_id: int):
    return {"message": f"Get issue blocker for issue {issue_id}"}


@router.put("/issue/{issue_id}/blocker")
async def update_issue_blocker(issue_id: int):
    return {"message": f"Update issue blocker for issue {issue_id}"}


@router.delete("/issue/{issue_id}/blocker")
async def delete_issue_blocker(issue_id: int):
    return {"message": f"Delete issue blocker for issue {issue_id}"}
