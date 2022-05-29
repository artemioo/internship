from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config
from ..models.banner import Banner


@view_config(route_name='banner_delete', permission='delete')
def banner_delete(request):
    banner_id = int(request.matchdict["id"])
    banner = request.dbsession.query(Banner).get(banner_id)
    request.dbsession.delete(banner)
    return HTTPFound(location=request.route_url('home'))
