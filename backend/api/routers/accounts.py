from fastapi import APIRouter


router = APIRouter(prefix="/v1")


# ==============================================================================
# Accounts CRUD endpoints
# ==============================================================================


@router.post("/account")
async def create_account():
    return {"message": "Create account"}


@router.get("/account/{account_id}")
async def get_account(account_id: int):
    return {"message": f"Get account {account_id}"}


@router.put("/account/{account_id}")
async def update_account(account_id: int):
    return {"message": f"Update account {account_id}"}


@router.delete("/account/{account_id}")
async def delete_account(account_id: int):
    return {"message": f"Delete account {account_id}"}
