import pyramid.view


API_VERSION = 0.1


@pyramid.view.view_defaults(renderer='json')
class HomeView(object):
    """Announce the api version at root path."""

    def __init__(self, request):
        self.request = request

    def __call__(self):
        response = ('You are using the schaukasten api '
                    'version {}.'.format(API_VERSION))
        return dict(success=response, version=API_VERSION)
