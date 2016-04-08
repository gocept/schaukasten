import pytest
import webtest
import schaukasten.browser.app


@pytest.fixture(scope='session')
def wsgi_app():
    """Create the schaukasten WSGI app."""
    schaukasten_app = schaukasten.browser.app.Schaukasten(testing=True)
    schaukasten_app.configure()
    return schaukasten_app({})


@pytest.fixture(scope='function')
def browser(wsgi_app):
    """Get a zope.testbrowser for the WSGI-APP."""
    return webtest.TestApp(wsgi_app)
