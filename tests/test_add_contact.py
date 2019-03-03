# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name='Roman',
                               last_name='Yatsenko',
                               company='ModulKassa',
                               address='Russia, Novosibirsk, Planetnaya st., 30',
                               mobile_phone='+79529316917',
                               email='test@test.ru',
                               notes='This is just a text for test of notes.'))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name='',
                               last_name='',
                               company='',
                               address='',
                               mobile_phone='',
                               email='',
                               notes=''))

