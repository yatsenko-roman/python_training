# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name='Roman',
                               last_name='Yatsenko',
                               company='ModulKassa',
                               mobile_phone='+79529316917',
                               email='test@test.ru',
                               notes='This is just a text for test of notes.'))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name='',
                               last_name='',
                               company='',
                               address='',
                               mobile_phone='',
                               email='',
                               notes=''))
    app.session.logout()

