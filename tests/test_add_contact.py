# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name='Roman',
                      last_name='Yatsenko',
                      company='ModulKassa',
                      address='Russia, Novosibirsk, Planetnaya st., 30',
                      mobile_phone='+79529316917',
                      email='test@test.ru',
                      notes='This is just a text for test of notes.')
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name='',
                      last_name='',
                      company='',
                      address='',
                      mobile_phone='',
                      email='',
                      notes='')
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
