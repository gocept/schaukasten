from schaukasten.db import ENGINE_NAME
import gocept.cache.method
import pytest
import risclog.sqlalchemy.testing


def cleanup():
    """Reset global state during tests.

    This cleanup step cannot be written as a fixture. It works for unit tests,
    but could not be reused for browser tests. I think that pytest executes it
    first against the unit test DB and won't trigger it a second time for the
    portal app database.

    """
    gocept.cache.method.clear()


@pytest.fixture(scope='session')
def database_session(request):
    """Set up and tear down the verdi.congress database.

    Returns the database utility object.
    """
    # create pytest fixture for database
    return risclog.sqlalchemy.testing.database_fixture_factory(
        request, 'schaukasten', ENGINE_NAME, create_all=True)


@pytest.fixture(scope='function')
def database(request, database_session):
    """Perform database setup and tear down for test function.

    Will empty all tables beforehand and close the session afterwards.

    Since this fixture is effectively used in every unit test, we also run the
    cleanup here.

    Returns the database utility object.
    """
    risclog.sqlalchemy.testing.database_test_livecycle_fixture_factory(request)
    cleanup()
    return database_session
