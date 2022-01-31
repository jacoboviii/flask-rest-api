from typing import Any, Dict, Optional

from resources.user import UserModel


def authenticate(username: str, password: str) -> UserModel:
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user


def identity(payload: Dict[str, Any]) -> Optional[UserModel]:
    user_id: int = payload["identity"]
    return UserModel.find_by_id(user_id)
