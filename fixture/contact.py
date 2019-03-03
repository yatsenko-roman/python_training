# -*- coding: utf-8 -*-

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value('firstname', contact.first_name)
        self.change_field_value('lastname', contact.last_name)
        self.change_field_value('company', contact.company)
        self.change_field_value('address', contact.address)
        self.change_field_value('mobile', contact.mobile_phone)
        self.change_field_value('email', contact.email)
        self.change_field_value('notes', contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        # submit contact deleting
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit contact updating
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
