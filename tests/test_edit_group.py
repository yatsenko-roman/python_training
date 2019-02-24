# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name='Name of group', header='This is new header', footer='This is new footer'))
    app.session.logout()

