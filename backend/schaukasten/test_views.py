from pyramid import testing


def test_views__HomeView__1():
    from .views import HomeView
    request = testing.DummyRequest()
    response = HomeView(request)()
    assert {'success': 'You are using the schaukasten api version 0.1.',
            'version': 0.1} == response
