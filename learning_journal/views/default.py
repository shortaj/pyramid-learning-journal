"""Views for the Learning Journal."""
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from datetime import date as Date
from pyramid.security import remember, forget
from learning_journal.security import check_credentials

from ..models import Entry


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2',
    require_csrf=False
)
def home_view(request):
    """The default home page view return."""
    list_entries = []
    entries = request.dbsession.query(Entry).order_by(Entry.date).all()
    list_entries.append(entries)
    return {'entries': list_entries}


@view_config(
    route_name='entry',
    renderer='../templates/single_entry.jinja2',
    require_csrf=False
)
def detail_view(request):
    """The default single-entry page view return."""
    try:
        e = request.dbsession.query(Entry).get(int(request.matchdict['id']))
    except IndexError:
        raise HTTPNotFound
    return {'entry': e}


@view_config(
    route_name='new_entry',
    renderer='../templates/new_entry.jinja2',
    permission='token',
    require_csrf=True
)
def new_entry_view(request):
    """The default home page view return."""
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        date = Date.today()
        new_entry = Entry(title=title, body=body, date=date)
        request.dbsession.add(new_entry)
        return HTTPFound(location=request.route_url('home'))
    elif request.method == 'GET':
        return {}
    return HTTPFound(location=request.route_url('home'))


@view_config(
    route_name='edit',
    renderer='../templates/edit_entry.jinja2',
    permission='token',
    require_csrf=True
)
def edit_entry_view(request):
    """Set the edit POST and GET http responses."""
    e = request.dbsession.query(Entry).get(request.matchdict['id'])
    if request.method == "POST":
        e.title = request.POST['title'].capitalize()
        e.body = request.POST['body']
        e.date = Date.today()
        request.dbsession.flush()
        return HTTPFound(location=request.route_url('entry', id=e.id))
    elif request.method == "GET":
        return {'entry': e}


@view_config(
    route_name='login',
    renderer='../templates/login.jinja2',
    require_csrf=False
)
def login_view(request):
    """Set the login route and view."""
    if request.method == "GET":
        return {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if check_credentials(username, password):
            headers = remember(request, username)
            return HTTPFound(location=request.route_url('home'), headers=headers)
        return {'error': 'Invalid username or password.'}


@view_config(
    route_name='logout',
    renderer='../templates/logout.jinja2',
    require_csrf=False
)
def logout_view(request):
    """."""
    headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)
