# СЕРВЕРНАЯ ЧАСТЬ

from fastapi import APIRouter, Request
from schemas import UnitCreateSchema, UnitUpdateSchema, UserCreateSchema, UserUpdateSchema, UserDeleteSchema
from models import UnitModel, UserDB
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert

# РОУТЕРЫ ДЛЯ СПИСКА ПОЛЬЗОВАТЕЛЕЙ (логины и пароли)

user_router = APIRouter(prefix='/api/v1/users')


@user_router.post('/register')
def create_user(request: Request, user: UserCreateSchema):
    new_user = UserDB(
        id = user.id,
        username = user.username,
        password = user.password,
    )
    session = Session(engine)
    session.add(new_user)
    # stmt = insert(UserDB).values(username=user.username,
    #                                  password=user.password,
    #                                  id=user.id)
    # session.execute(stmt)
    session.commit()
    session.close()
    print(user)
    return {'user': user}


@user_router.get('/get_users')
def get_users_list(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(UserDB) # (sql запрос по форме запросить таблицу unit модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    users:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return users


@user_router.put('/update_user') # можно на один адрес разные методы накидывать
def update_user(request: Request, user_id: int, user_update: UserUpdateSchema): # unit_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(UserDB).where(UserDB.id==user_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    user = object_db.scalars().first()
    user.title = user_update.username
    user.passwoed = user_update.password
    session.merge(user) # обновит существующий через мердж
    session.commit()
    session.close()
    return user_update


@user_router.delete('/delete_user')
def delete_user(request: Request, user_id: int):
    session = Session(engine)
    stmt = select(UserDB).where(UserDB.id==user_id) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    user = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(user)
    session.commit()
    session.close()
    return {'message': f'Пользователь под номером {user_id} удалён.'}


# РОУТЕРЫ ДЛЯ СПИСКА ЕДИНИЦ


unit_router = APIRouter(prefix='/api/v1/units') # префикс для разработчика чисто, чтобы понимали что тут находится какой-то интерфейс 


@unit_router.post('/create_unit')
def create_unit(request: Request, unit: UnitCreateSchema):
    session = Session(engine) # экземпляр класса, который позволяет подключиться к БД
    stmt = insert(UnitModel).values(title=unit.title,  # insert импортируется из sqlalchemy,
                                    description=unit.description) # нельзя чтобы в строке не было больше 80 символов ПРАВИЛО ХОРОШЕГО ТОНА, можно включить в настройках)
    session.execute(stmt)
    session.commit() #сделалит сохранение, без КОММИТА не сохранится! как dump в джсоне
    session.close()
    return unit


@unit_router.get('/get_unit')
def get_unit(request: Request): #Этот реквест нужно обязательно прописывать, в некоторых гайдах его нет
    session = Session(engine)# экземпляр класса, отвечающий за соединение с базой данных
    stmt = select(UnitModel) # (sql запрос по форме запросить таблицу unit модел)
    object_db = session.execute(stmt) #формируется скл объект, получаем объект с базы данных (всю табличку дёрнет, получим объект но работать с ним не сможем, надо преобразовать)
    units:list = object_db.scalars().all() # скалларс преобразует всё это в понятный нам тип список, по-другому бы не получилось работать с ним
    session.close()
    return units # закрыли сессию и возвращаем список



@unit_router.put('/update_unit') # можно на один адрес разные методы накидывать
def update_unit(request: Request, unit_title: str, unit_update: UnitUpdateSchema): # unit_id:int получаем айди к изменению у пользователя, 
    session = Session(engine)
    stmt = select(UnitModel).where(UnitModel.title==unit_title) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    print(object_db)
    unit = object_db.scalars().first()
    unit.title = unit_update.title
    unit.description = unit_update.description
    session.merge(unit) # обновит существующий через мердж
    session.commit()
    session.close()
    return unit_update

@unit_router.delete('/delete_unit/')
def delete_unit(request: Request, unit_title: str):
    session = Session(engine)
    stmt = select(UnitModel).where(UnitModel.title==unit_title) # формируем запрос: мы хотим получить из таблички таск модел запись по айдишнику
    object_db = session.execute(stmt)
    unit = object_db.scalar() # .one() один объект из списка извлекает
    session.delete(unit)
    session.commit()
    session.close()
    return {'message': f'Единица под названием {unit_title} была удалена.'}