# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name='New first name'))

def test_modify_contact_last_name(app):
    app.contact.modify_first_contact(Contact(last_name='New last name'))

def test_modify_contact_company(app):
    app.contact.modify_first_contact(Contact(company='New company'))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address='New address'))
