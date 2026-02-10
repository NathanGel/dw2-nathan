from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    name: str
    location: str

    def validate_user(self) -> bool:
        return bool(self.name and self.location)