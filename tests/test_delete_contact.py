# -*- coding: utf-8 -*-

from model.contact import Contact
import time
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='Test'))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(5)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

