"""Test for learning journal."""
from pyramid import testing
from pyramid.response import Response
import pytest
import os
import io


HERE = os.path.dirname(__file__)


@pytest.fixture
def httprequest():
    """Ger."""
    req = testing.DummyRequest()
    return req


def test_return_of_views_are_responses(httprequest):
    """."""
    from learning_journal.views.default import (
        list_view,
        detail_view,
        new_entry_view,
        edit_entry_view
    )
    list_response = list_view(httprequest)
    detail_response = detail_view(httprequest)
    new_entry_response = new_entry_view(httprequest)
    edit_entry_response = edit_entry_view(httprequest)
    assert isinstance(list_response, Response)
    assert isinstance(detail_response, Response)
    assert isinstance(new_entry_response, Response)
    assert isinstance(edit_entry_response, Response)


def test_html_content_in_response_index(httprequest):
    """."""
    from learning_journal.views.default import list_view
    with io.open(os.path.join(HERE, 'templates/index.jinja2')) as the_file:
        file_content = the_file.read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_new_entry(httprequest):
    """."""
    from .views.default import create_view
    with io.open(os.path.join(HERE, 'templates/new_entry.html')) as the_file:
        file_content = the_file.read()
    response = create_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_single_entry(httprequest):
    """."""
    from .views.default import detail_view
    with io.open(os.path.join(HERE, 'templates/single_entry.html')) as the_file:
        file_content = the_file.read()
    response = detail_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_edit_entry(httprequest):
    """."""
    from learning_journal.views.default import update_view
    with io.open(os.path.join(HERE, 'templates/edit_entry.html')) as the_file:
        file_content = the_file.read()
    response = update_view(httprequest)
    assert file_content == response.text


def test_response_status_code(httprequest):
    """."""
    from learning_journal.views.default import list_view
    response = list_view(httprequest)
    assert response.status_code == 200
