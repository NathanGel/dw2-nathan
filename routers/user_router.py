from fastapi import APIRouter, HTTPException
from services import user_service
from models import user

router = APIRouter()

@router.get('/user/{user_id}')
def get(user_id: int):
    try:
        return user_service.get_user_by_id(user_id)
    except KeyError as ke:
        return HTTPException(status_code=404, detail=ke.args[0])
    except:
        return HTTPException(status_code=500, detail="An unexpected error occured please try again later")
    
@router.post('/user')
def post(user: user.User):
    try:
        return user_service.create_user(user)
    except ValueError as ve:
        return HTTPException(status_code=422, detail=ve.args[0])
    except:
        return HTTPException(status_code=500, detail="An unexpected error occured please try again later")
