from repositories import user_repository
from models import user

def get_user_by_id(id: int):
    if id <= 0:
        raise ValueError(f"The given ID {id} is invalid")
    return user_repository._get_user_by_id(id)

def get_all_users():
    return user_repository._get_all_users()

def create_user(user: user.User):
    isValid = user.validate_user()
    if not isValid:
        raise ValueError(f"Name and location are required")
    user = user_repository._create_user(user)
    return user

def update_user(user: user.User): 
    isValid = user.validate_user()
    if not isValid:
        raise ValueError(f"Name and location are requiured")
    user = user_repository._update_user(user)
    return user

def remove_user(id: int):
    user_repository._remove_user(id)