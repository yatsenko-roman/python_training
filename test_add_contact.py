# -*- coding: utf-8 -*-

import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name='Roman',
                                   last_name='Yatsenko',
                                   company='ModulKassa',
                                   address='Russia, Novosibirsk, Planetnaya st., 30',
                                   mobile_phone='+79529316917',
                                   email='test@test.ru',
                                   notes='This is just a text for test of notes.'))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(first_name='',
                                   last_name='',
                                   company='',
                                   address='',
                                   mobile_phone='',
                                   email='',
                                   notes=''))
    app.logout()

