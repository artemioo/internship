from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authentication_policy = AuthTktAuthenticationPolicy('somesecret')  # будет использоваться для подписи куки
    authorization_policy = ACLAuthorizationPolicy()

    with Configurator(settings=settings,
                      authentication_policy=authentication_policy,
                      authorization_policy=authorization_policy) as config:
        config.include('pyramid_mako')
        config.include('.routes')
        config.include('.models')
        config.scan()
    return config.make_wsgi_app()
