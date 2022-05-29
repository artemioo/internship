from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config
from ..forms import BannerUpdateForm
from ..models.banner import Banner


@view_config(route_name='banner_update',
             renderer='banner_editor:templates/admin/banner_update.mako', permission='create')
def banner_update(request):
    banner_id = int(request.params.get('id', -1))  # получаем id
    banner = request.dbsession.query(Banner).get(banner_id) # достаем нужный баннер
    if not banner:  # если его нет - ошибка 404
        raise HTTPNotFound
    form = BannerUpdateForm(request.POST, banner)  # генерим форму с данными нашего баннера
    if request.method == 'POST' and form.validate():
        del form.id  # (идет перезапись ключа)
        form.populate_obj(banner)
        return HTTPFound(
            location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}
