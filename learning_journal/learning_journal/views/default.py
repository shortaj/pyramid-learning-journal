"""Views for the Learning Journal."""
from pyramid.response import Response
import io
import os


HERE = os.path.dirname(__file__)


def list_view(request):
    """The default home page view return."""
    with io.open(os.path.join(HERE, '../templates/index.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def detail_view(request):
    """The default single entry page view return."""
    with io.open(os.path.join(HERE, '../templates/single_entry.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def create_view(request):
    """The default new entry page view return."""
    with io.open(os.path.join(HERE, '../templates/new_entry.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)


def update_view(request):
    """The default edit entry page view return."""
    with io.open(os.path.join(HERE, '../templates/edit_entry.html')) as the_file:
        imported_text = the_file.read()
    return Response(imported_text)
