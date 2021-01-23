from fastapi import APIRouter

router = APIRouter()


@router.get("/me")
async def read_user_me():
    return {"user_id": 'Mee'}


@router.get("/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
