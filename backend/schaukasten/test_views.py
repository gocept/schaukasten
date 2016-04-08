from pyramid import testing


def test_views__HomeView__1():
    from .views import HomeView
    request = testing.DummyRequest()
    response = HomeView(request)()
    assert {'success': 'You have asked no_server:no_port and '
            'got the answer 84/2.'} == response
