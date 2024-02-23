from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_adin():
    return {"message": "Admin getting schwifty"}