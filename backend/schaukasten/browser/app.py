from schaukasten.db import ENGINE_NAME
from schaukasten.views import HomeView, UploadView
import pyramid.events
import pyramid.httpexceptions
import pyramid.paster
import pyramid.registry
import pyramid.security
import pyramid.view
import risclog.sqlalchemy.db


class Schaukasten(object):
    """The schaukasten application."""

    settings = None

    def __init__(self, testing=False, **settings):
        self.settings = settings
        self.settings['testing'] = testing
        self.testing = testing

    def __call__(self, global_config, **settings):
        self.settings.update(settings)
        self.configure()
        self.setup_runtime()
        # can't go into setup_runtime, since initialize_db uses that, too
        return self.make_wsgi_app(global_config)

    def setup_runtime(self):
        if not self.testing:
            db = risclog.sqlalchemy.db.get_database()
            db.register_engine(self.settings['sqlalchemy.url'],
                               name=ENGINE_NAME,
                               alembic_location='schaukasten:alembic')

    def make_wsgi_app(self, global_config):
        app = self.config.make_wsgi_app()
        return app

    def configure(self):
        self.config = config = pyramid.config.Configurator(
            settings=self.settings)
        config.setup_registry(settings=self.settings)
        config.include('pyramid_tm')

        config.set_default_permission('view')
        self.add_views()
        self.add_routes()

    def add_routes(self):
        config = self.config
        config.add_route('api', '/api/')
        config.add_route('files', '/api/files')

    def add_views(self):
        config = self.config
        config.add_view(HomeView, route_name='api')
        config.add_view(
            UploadView,
            route_name='files',
            request_method='POST')

factory = Schaukasten()
