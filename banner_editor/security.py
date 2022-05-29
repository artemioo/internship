from pyramid.security import Allow, Everyone, Authenticated


class BannerRecordFactory(object):
    __acl__ = [(Allow, Everyone, 'view'),  # у всех есть доступ к просмотру, и у залогиненых создать и ред.
               (Allow, Authenticated, 'create'),
               (Allow, Authenticated, 'edit'),
               (Allow, Authenticated, 'delete'), ]

    def __init__(self, request):
        pass

