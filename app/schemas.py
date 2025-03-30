from pydantic import BaseModel, Field, ConfigDict
from typing import List
# from models import UnitDB
# ------------------------------ СОЗДАВАЛКА ДЕФОЛТНОЙ ЕДИНИЦЫ -------------------------------------------
def create_default_unit():
    # return[UnitDB(name='unit-1')]
    return[UnitCreateSchema(title='unit-1')]
# ------------------------------ СОЗДАВАЛКА ДЕФОЛТНОЙ ЕДИНИЦЫ -------------------------------------------

# СХЕМЫ ПОЛЬЗОВАТЕЛЕЙ
# По ним мы принимаем данные у пользователя с формы

class UserCreateSchema(BaseModel):
    username: str
    password: str

"""
class UserUpdateSchema(BaseModel):
    username: str
    password: str
    
class UserDeleteSchema(BaseModel):
    id: int
"""
    

# СХЕМЫ ЕДИНИЦ

class UnitCreateSchema(BaseModel):
    title: str = Field(..., title='Unit Title', max_length=50)

class UnitUpdateSchema(BaseModel):
    title: str
    
class UnitDeleteChema(BaseModel):
    title: str
    
class Unit(BaseModel):
    id: int
    title: str
    project_id : int
    
    model_config = ConfigDict(from_attributes=True)

# СХЕМЫ ПРОЕКТОВ

class ProjectCreateSchema(BaseModel):
    title: str = Field(..., title='Project Title', max_length=50)
    units: List[UnitCreateSchema] = Field(default_factory=create_default_unit, title='Units')
    
    class Config:
        json_schema_extra = {
            'example': {'title': 'My Awesome Project',
                    'units': [{'title': 'unit-1'}]}
        }
    
class Project(BaseModel):
    id: int
    title: str
    model_config = ConfigDict(from_attributes=True)
