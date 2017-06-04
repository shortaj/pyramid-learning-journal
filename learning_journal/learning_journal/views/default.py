"""Views for the Learning Journal."""
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound
from learning_journal.data.journal import JOURNAL


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2'
)
def list_view(request):
    """The default home page view return."""
    return {'id': '',
            'title': '',
            'date-created': '',
            }


@view_config(
    route_name='entry',
    renderer='../templates/single_entry.jinja2'
)
def detail_view(request):
    """The default home page view return."""
    the_id = request.matchdict['id']
    try:
        journals = JOURNAL[the_id]
    except IndexError:
        raise HTTPNotFound
    return {
        'journals': journals
    }


@view_config(
    route_name='new-entry',
    renderer='../templates/new_entry.jinja2'
)
def new_entry_view(request):
    """The default home page view return."""
    return {'id': '',
            'title': '',
            'date-created': '',
            'body': '',
            }


@view_config(
    route_name='edit',
    renderer='../templates/edit_entry.jinja2'
)
def edit_entry_view(request):
    """The default home page view return."""
    return {'id': '',
            'title': '',
            'date-created': '',
            'body': '',
            }
