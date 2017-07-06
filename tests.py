"""Test for learning journal."""
from pyramid import testing
from pyramid.response import Response
import pytest


@pytest.fixture
def httprequest():
    """Ger."""
    req = testing.DummyRequest()
    return req


def test_return_of_views_are_responses(httprequest):
    """."""
    from pyramid_learning_journal.views.default import (
        list_view,
        detail_view,
        create_view,
        update_view
    )
    assert isinstance(list_view(httprequest), Response)
    assert isinstance(detail_view(httprequest), Response)
    assert isinstance(create_view(httprequest), Response)
    assert isinstance(update_view(httprequest), Response)


def test_html_content_in_response_index(httprequest):
    """."""
    from pyramid_learning_journal.views.default import list_view
    file_content = open('/templates/index.html').read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_new_entry(httprequest):
    """."""
    from pyramid_learning_journal.views.default import list_view
    file_content = open('/templates/new_entry.html').read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_single_entry(httprequest):
    """."""
    from pyramid_learning_journal.views.default import list_view
    file_content = open('/templates/single_entry.html').read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_html_content_in_response_edit_entry(httprequest):
    """."""
    from pyramid_learning_journal.views.default import list_view
    file_content = open('/templates/edit_entry.html').read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_response_status_code(httprequest):
    """."""
    from pyramid_learning_journal.views.default import list_view
    response = list_view(httprequest)
    assert response.status_code == 200
