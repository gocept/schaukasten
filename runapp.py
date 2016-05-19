from paste.deploy import loadapp
from waitress import serve


if __name__ == "__main__":
    app = loadapp('config:heroku.ini', relative_to='backend')
    open('/tmp/app-initialized', 'w')

    serve(app, host='127.0.0.1', port=5000)
