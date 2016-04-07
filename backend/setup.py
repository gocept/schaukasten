from setuptools import setup, find_packages

requires = [
    'alembic',
    'pyramid',
    'pyramid_tm',
    'sqlalchemy',
    'risclog.sqlalchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pytest',
    'pytest-sugar',
    'pytest-flake8',
    'pytest-cov',
    ]

test_requires = [
    'pytest',
    ]

setup(name='schaukasten',
      version='0.0',
      description='schaukasten',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='gocept gmbh & co. kg',
      author_email='mail@gocept.com',
      url='https://github.com/gocept/schaukasten',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='schaukasten',
      install_requires=requires,
      extras_require={
        'test': test_requires,
      },
      entry_points={
        'paste.app_factory': [
            'main=schaukasten.browser.app:factory'
        ],
      },
      )
