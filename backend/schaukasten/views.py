import pyramid.view


@pyramid.view.view_defaults(renderer='json')
class HomeView(object):
    """Initial view for homepage."""

    def __init__(self, request):
        self.request = request

    def __call__(self):
        environ = self.request.environ
        server_name = environ.get('SERVER_NAME', 'no_server')
        server_port = environ.get('SERVER_PORT', 'no_port')
        response = ('You have asked {}:{} and got the answer '
                    '84/2.'.format(server_name, server_port))
        return dict(success=response)
