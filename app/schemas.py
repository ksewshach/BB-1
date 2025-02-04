from pydantic import BaseModel

# СХЕМЫ ПОЛЬЗОВАТЕЛЕЙ
# По ним мы принимаем данные у пользователя с формы

class UserCreateSchema(BaseModel):
    username: str
    password: str

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


