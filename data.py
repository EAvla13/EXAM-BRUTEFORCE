from pydantic import BaseModel
from typing import Optional

class Userlogin(BaseModel):
    id: Optional[int] = None
    username: str
    password:str
    is_active: Optional[bool] = True
