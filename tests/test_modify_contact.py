# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name='New first name')
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_modify_contact_last_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name='Test'))
#     app.contact.modify_first_contact(Contact(last_name='New last name'))
#
# def test_modify_contact_company(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name='Test'))
#     app.contact.modify_first_contact(Contact(company='New company'))
#
# def test_modify_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name='Test'))
#     app.contact.modify_first_contact(Contact(address='New address'))
