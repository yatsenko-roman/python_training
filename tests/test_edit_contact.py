# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name='Angelina',
                               last_name='Jolie',
                               company='Avanpost',
                               address='Russia, Novosibirsk, Planetnaya st., 30',
                               mobile_phone='+79529316918',
                               email='test1@test1.ru',
                               notes='This is new note text.'))
    app.session.logout()