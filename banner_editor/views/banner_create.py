from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config
from ..forms import BannerCreateForm
from ..models.banner import Banner


@view_config(route_name='banner_create',
             renderer='banner_editor:templates/admin/banner_create.mako', permission='create')
def banner_create(request):
    entry = Banner()
    form = BannerCreateForm(request.POST)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        request.dbsession.add(entry)
        return HTTPFound(location=request.route_url('home')) #добавляем форму и редирект на главную
    return {'form': form, 'action': request.matchdict.get('action')}
