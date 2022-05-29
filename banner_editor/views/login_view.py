from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from ..services.user import UserService


@view_config(route_name='admin', renderer='banner_editor:templates/admin/admin.mako')
def admin(request):
    return {}


@view_config(route_name='auth_login', renderer='string', request_method='POST')
def auth_login(request):
    username = request.POST.get('username') # достаем из словаря гет значение ключа имя пользователя
    if username:
        user = UserService.by_name(username, request=request) # если юзер есть, кладем в переменную user
        if user:  # если все ок( и совпало значение пароля)
            headers = remember(request, user.name)
            #  создается новый набор заголовков (который используется для установки файла cookie)
        else:
            headers = forget(request)
            HTTPFound(location=request.route_url('admin'), headers=headers)
    else:
        headers = forget(request)
    return HTTPFound(location=request.route_url('editor'), headers=headers)
