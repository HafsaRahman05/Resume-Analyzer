from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    email: str
    profession: Optional[str] = None
