from pyramid.view import view_config
from sqlalchemy import desc, asc
from ..models.banner import Banner
from ..services.banner_paginator import BannerRecordService


@view_config(route_name='editor', permission='create', renderer='banner_editor:templates/admin/editor.mako')
def editor(request):
    sort = request.params.get('sort', Banner.position)
    size = int(request.params.get('size', 3))
    sort_type = request.params.get('dir', desc)
    filter_type = request.params.get('filter_type', None)

    if sort_type == 'asc':
        sort_asc_desc = 'desc'
        if filter_type:
            banners = request.dbsession.query(Banner).order_by(asc(sort)).filter(Banner.status == filter_type)
        else:
            banners = request.dbsession.query(Banner).order_by(asc(sort))
    else:
        sort_asc_desc = 'asc'
        if filter_type:
            banners = request.dbsession.query(Banner).order_by(desc(sort)).filter(Banner.status == filter_type)
        else:
            banners = request.dbsession.query(Banner).order_by(desc(sort))

    page = int(request.params.get('page', 1))
    paginator = BannerRecordService.get_paginator(request, banners, size, page)

    return {'paginator': paginator, 'sort_type': sort_type, 'sort_asc_desc': sort_asc_desc, 'filter_type': filter_type}

    # test = request.GET
    # test1 = request.params









