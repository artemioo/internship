from pyramid.view import view_config
from ..models.banner import Banner, BannerStatus


@view_config(route_name='home',
             renderer='banner_editor:/templates/public/home.mako')
def index_page(request):
    query = request.dbsession.query(Banner).\
        filter(Banner.status == BannerStatus.Enabled.value).order_by(Banner.position) # список всех баннеров по приоритету и статусу
    return {'query': query}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
