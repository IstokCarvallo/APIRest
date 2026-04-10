from fastapi import APIRouter
from app.application.services.user_service import UserService

router = APIRouter()
service = UserService()

@router.get("/users")
def get_users():
    return service.get_users()