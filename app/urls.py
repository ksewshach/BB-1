# КЛИЕНТСКАЯ ЧАСТЬ

from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

template = Jinja2Templates(directory='templates')


user_url = APIRouter(tags=["user"]) # чтобы красиво отображались в категории в доксе вместо default сверзу

@user_url.get(path='/test/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='test.html',
    )
    
@user_url.get(path='/notes/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='notes.html',
    )
    
@user_url.get(path='/characters/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='characters.html',
    )

@user_url.get(path='/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='homepage.html',
    )

@user_url.get(path='/login/')
def login(request: Request):
    return template.TemplateResponse(
        request=request,
        name='login_page.html',
    )

@user_url.get(path='/register/')
def register(request: Request):
    return template.TemplateResponse(
        request=request,
        name='registration_page.html',
    )

@user_url.get(path='/my_projects/')
def my_projects(request: Request):
    return template.TemplateResponse(
        request=request,
        name='my_projects.html',
    )
@user_url.get(path='/project/')
def create_project(request: Request):
    return template.TemplateResponse(
        request=request,
        name='project.html',
    )
