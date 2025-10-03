from pydantic import BaseModel

class Userlogin(BaseModel):
    id: int
    username: str
    password:str
    is_active: bool

class UserUpdate(BaseModel):
    username: str = None
    password: str = None
    is_active: bool = None
