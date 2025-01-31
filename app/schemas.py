from pydantic import BaseModel

# СХЕМЫ ПОЛЬЗОВАТЕЛЕЙ

class UserCreateSchema(BaseModel):
    username: str
    password: str
    # id: int
    
class UserUpdateSchema(BaseModel):
    username: str
    password: str
    
class UserDeleteSchema(BaseModel):
    id: int
    
# СХЕМЫ ЕДИНИЦ

class UnitCreateSchema(BaseModel):
    title: str
    description: str
    # id: int

class UnitUpdateSchema(BaseModel):
    title: str
    description: str
    
class UnitDeleteChema(BaseModel):
    title: str


