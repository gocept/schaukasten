from pyramid import testing


def test_views__HomeView__1():
    from .views import HomeView
    request = testing.DummyRequest()
    response = HomeView(request)()
    assert {'msg': 'You are using the schaukasten api version 0.1.',
            'status': 'success',
            'version': 0.1} == response
