def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('admin', '/admin/')
    config.add_route('banner_info', '/admin/banner/{id:\d+}',
                     factory='banner_editor.security.BannerRecordFactory')
    config.add_route('banner_create', '/admin/banner/create/',
                     factory='banner_editor.security.BannerRecordFactory')
    config.add_route('banner_update', '/admin/banner/update/',
                     factory='banner_editor.security.BannerRecordFactory')
    config.add_route('banner_delete', '/admin/banner/delete/{id:\d+}',
                     factory='banner_editor.security.BannerRecordFactory')
    config.add_route('auth_login', '/auth/login/')
    config.add_route('auth_logout', '/auth/logout/')
    config.add_route('editor', '/admin/editor/',
                     factory='banner_editor.security.BannerRecordFactory')





