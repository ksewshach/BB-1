# СЕРВЕРНАЯ ЧАСТЬ

from fastapi import APIRouter, Request, Depends
from schemas import UnitCreateSchema, UnitUpdateSchema, ProjectCreateSchema, UserCreateSchema
from database import SessionLocal
from models import UnitDB, UserDB, ProjectDB
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert
import random
from typing  import List, Optional
import sqlite3

# РОУТЕРЫ ДЛЯ СПИСКА ПОЛЬЗОВАТЕЛЕЙ (логины и пароли)

user_router = APIRouter(prefix='/api/v1/users')
auth_router = APIRouter(prefix='/api/v1/users')

@user_router.post('/register/')
def create_user(request: Request, user: UserCreateSchema):
    def generate_unique_id(session):
        while True:
            user_id = random.randint(100000, 999999)
            if session.scalar(select(UserDB).where(UserDB.id == user_id)) is None:
                return user_id
    session = Session(engine)
    print(f"Сгенерирован ID: {id}")  
    new_user = UserDB(
        id = generate_unique_id(session),
        username = user.username,
        password = user.password,
    )
    session.add(new_user)
    session.commit()
    session.close()
    return {"user": user}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
            
@user_router.post('/my_projects/', response_model=ProjectCreateSchema)
def create_project(request: Request, project: ProjectCreateSchema, db: Session = Depends(get_db)):
    new_project = ProjectDB(title=project.title)
    # Создаём единицы
    for unit_data in project.units:
        unit = UnitDB(title=unit_data.title, project=new_project)
        db.add(unit)
        
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    print(f'Создан новый проект с ID: {project.id}')
    return project

@auth_router.post('/login/')
def login(request: Request):
    pass

@user_router.get('/get_users/')
def get_users_list(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(UserDB) # (sql запрос по форме запросить таблицу unit модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    users:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return users


"""
@user_router.put('/update_user/') # можно на один адрес разные методы накидывать
def update_user(request: Request, user_id: int, user_update: UserUpdateSchema): # unit_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(UserDB).where(UserDB.id==user_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    user = object_db.scalars().first()
    user.title = user_update.username
    user.password = user_update.password
    session.merge(user) # обновит существующий через мердж
    session.commit()
    session.close()
    return user_update
"""

@user_router.delete('/delete_user/')
def delete_user(request: Request, user_id: int):
    session = Session(engine)
    stmt = select(UserDB).where(UserDB.id==user_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    user = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(user)
    session.commit()
    session.close()
    return {'message': f'Пользователь под номером {user_id} удалён.'}


# ----------------------------------TO DO'S--------------------------------------
"""      
    session = Session(engine) # экземпляр класса, который позволяет подключиться к БД
    stmt = insert(ProjectDB).values(title=project.title,  # insert импортируется из sqlalchemy,
                                    owner_id=project.owner_id) # нельзя чтобы в строке не было больше 80 символов ПРАВИЛО ХОРОШЕГО ТОНА, можно включить в настройках)
    session.execute(stmt)
    session.commit() #сделалит сохранение, без КОММИТА не сохранится! как dump в джсоне
    session.close()
    return project
    """

        
"""

    @user_router.post('/create_unit/')
    def create_unit(request: Request, unit: UnitCreateSchema):
        
        # ПРОВЕРИМ CREATE_ALL мб тут sql запрос для создания новой таблицы.
        
        session = Session(engine) # экземпляр класса, который позволяет подключиться к БД
        stmt = insert(UnitDB).values(title=unit.title,  # insert импортируется из sqlalchemy,
                                        owner_id=unit.owner_id) # нельзя чтобы в строке не было больше 80 символов ПРАВИЛО ХОРОШЕГО ТОНА, можно включить в настройках)
        session.execute(stmt)
        session.commit() #сделалит сохранение, без КОММИТА не сохранится! как dump в джсоне
        session.close()
        return unit

@user_router.get('/list')
def get_list_task(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(TaskModel) # (sql запрос по форме запросить таблицу таск модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    tasks:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return tasks # закрыли сессию и возвращаем список

@user_router.post('/create')
def create_task(request: Request, task: TaskCreateSchema):
    session = Session(engine) # экземпляр класса, который позволяет подключиться к БД
    stmt = insert(TaskModel).values(title=task.title,  # insert импортируется из sqlalchemy,
                                    description=task.description) # нельзя чтобы в строке не было больше 80 символов ПРАВИЛО ХОРОШЕГО ТОНА, можно включить в настройках)
    session.execute(stmt)
    session.commit() #сделалит сохранение, без КОММИТА не сохранится! как dump в джсоне
    session.close()
    return task

@user_router.put('/list/') # можно на один адрес разные методы накидывать
def update_task(request: Request, task_id: int, task_change: TaskUpdateSchema): # task_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    task = object_db.scalars().first()
    task.title = task_change.title
    task.description = task_change.description
    task.status = task_change.status
    session.merge(task) # обновит существующий через мердж
    session.commit()
    session.close()
    return task_change

@user_router.delete('/delete/')
def delete_task(request: Request, task_id: int):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id==task_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    task = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(task)
    session.commit()
    session.close()
    return {'message': f'task id: {task_id} delete'}
    
    """
# ----------------------------------TO DO'S--------------------------------------

"""
@user_router.get('/get_unit/')
def get_unit(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(UnitDB) # (sql запрос по форме запросить таблицу unit модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    units:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return units # закрыли сессию и возвращаем список



@user_router.put('/update_unit/') # можно на один адрес разные методы накидывать
def update_unit(request: Request, unit_title: str, unit_update: UnitUpdateSchema): # unit_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(UnitDB).where(UnitDB.title==unit_title) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    unit = object_db.scalars().first()
    unit.title = unit_update.title
    unit.description = unit_update.description
    session.merge(unit) # обновит существующий через мердж
    session.commit()
    session.close()
    return unit_update

@user_router.delete('/delete_unit/')
def delete_unit(request: Request, unit_title: str):
    session = Session(engine)
    stmt = select(UnitDB).where(UnitDB.title==unit_title) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    unit = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(unit)
    session.commit()
    session.close()
    return {'message': f'Единица под названием {unit_title} была удалена.'}
    
    """