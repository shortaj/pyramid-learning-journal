"""Initialize the package."""
from pyramid.config import Configurator


def main(global_config, **settings):
    """The function returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
