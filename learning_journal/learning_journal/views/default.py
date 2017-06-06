"""Views for the Learning Journal."""
from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPFound
from datetime import date as Date

from ..models import Entry


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2'
)
def home_view(request):
    """The default home page view return."""
    entries = request.dbsession.query(Entry).order_by(Entry.date).all()
    return {'entries': entries}


@view_config(
    route_name='entry',
    renderer='../templates/single_entry.jinja2'
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
    renderer='../templates/new_entry.jinja2'
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
    renderer='../templates/edit_entry.jinja2'
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
