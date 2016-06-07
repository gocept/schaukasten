from schaukasten.file import Content, File
import os
import pyramid.view


API_VERSION = 0.1


@pyramid.view.view_defaults(renderer='json')
class BaseView(object):
    """Base class for schaukasten views. Renders JSON output"""

    def __init__(self, request):
        self.request = request


class HomeView(BaseView):
    """Announce the api version at root path."""

    def __call__(self):
        response = ('You are using the schaukasten api '
                    'version {}.'.format(API_VERSION))
        return dict(success=response, version=API_VERSION)


class UploadView(BaseView):
    """Handle the uploaded file and save in the database."""

    def __call__(self):

        if 'file_input' not in self.request.json:
            return dict(status='error', msg='No file uploaded', code=1)

        try:
            filename = os.path.basename(
                self.request.json['file_input']['filename'])
            input_file = self.request.json['file_input']['file']
        except KeyError:
            response = dict(
                status='error',
                msg='Wrong input parameters.',
                code=2
            )

        try:
            content = Content.create(raw_content=input_file)
            file_ = File.create(filename=filename, content=content)
            response = dict(
                status='success',
                filename=filename,
                file=str(file_.id),
            )
        except Exception:
            response = dict(
                status='error',
                msg='Error while uploading',
                code=3
            )

        return response
