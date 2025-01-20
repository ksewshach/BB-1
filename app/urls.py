# КЛИЕНТСКАЯ ЧАСТЬ

from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

template = Jinja2Templates(directory='templates')


# URL-ы ПОЛЬЗОВАТЕЛЕЙ

user_url = APIRouter(tags=["user"]) # чтобы красиво отображались в категории в доксе вместо default сверзу

@user_url.get(path='/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='homepage.html',
    )

@user_url.get(path='/login')
def login(request: Request):
    return template.TemplateResponse(
        request=request,
        name='login_page.html',
    )

@user_url.get(path='/register')
def register(request: Request):
    return template.TemplateResponse(
        request=request,
        name='registration_page.html',
    )
