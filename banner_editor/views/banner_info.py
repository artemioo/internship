from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config

from ..models.banner import Banner


@view_config(route_name='banner_info', renderer='banner_editor:templates/admin/banner_view.mako')
def banner_view(request):
    banner_id = int(request.matchdict.get('id'))
    try:
        banner = request.dbsession.query(Banner).get(banner_id) # достаем нужный баннер
        return {'banner': banner}
    except ValueError:
        raise HTTPNotFound()

