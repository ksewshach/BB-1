# main - запускает сервер, тут вся ключевая логика по запуску сервера

import uvicorn
import sqlite3
from database import Base, engine
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from routers import user_router # auth_router
import urls
import routers

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    # Middleware(SessionMiddleware, secret_key='your_secret_key'), # ОЧЕНЬ ВАЖНО поменять эту строку на настоящий секретный ключ, но не в коде.
    title="BookBook",
    version="0.0.1",
)

app.mount('/static', StaticFiles(directory='static'), name='static') # static - хтмл и ксс, подгружает статику из директории
app.include_router(routers.user_router)
# app.include_router(routers.auth_router)
app.include_router(urls.user_url)


origins = ['*']

# origins = [
#     'http://localhost:8000', # Разрешаем запросв с локального хоста
#     'http://127.0.0.1:8000',
#     'http://localhost:5500',
#     'http://127.0.0.1:5500' # Разрешаем запросы с Live Server VS Code
# ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    # allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_methods=["*"], # Звёздочка разрешает всн запросы
    allow_headers=["*"]
)





if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # UnitModel.metadata.create_all(engine)
    print('Сервер запущен.')
    uvicorn.run('main:app', port=8000, host='127.0.0.1', reload=True)
    print('Сервер остановлен.')
