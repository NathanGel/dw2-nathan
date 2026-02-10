from models.user import User

users = {}

def _create_user(user: User):
    id = len(users) + 1
    user.id = id
    users[id] = user
    return user

def _remove_user(id: int):
    if id not in users:
        raise KeyError(f"User {id} not found")
    del users[id]

def _update_user(user: User): 
    if user.id not in users:
        raise KeyError(f"User {user.id} not found")
    users[user.id] = user
    return user

def _get_user_by_id(id: int):
    if id not in users:
        raise KeyError(f"User {id} not found")
    return users[id]

def _get_all_users():
    return users