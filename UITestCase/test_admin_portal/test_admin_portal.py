# Author: Yi Sun(Tim) 2023-08-29

'''Admin Page - Pytest Version'''

import pytest
from UIModule.admin_portal import AdminPage
# from UIModule.base_test import BaseTest

class Test_Admin_Portal():

    def test_admin_portal_001(self,admin_page):
        '''Verify the url of Admin login Page'''
        assert "sighte" in admin_page.get_url.lower()

    def test_admin_portal_002(self,admin_page):
        '''Verify the default Sections in Admin login Page'''
        add_menu, list_menu, account_menu = admin_page.check_default_menu
        assert "ADD" in add_menu
        assert "LIST" in list_menu
        assert "ACCOUNT" in account_menu

    def test_admin_portal_003(self,admin_page):
        '''Verify the Find Quote in Admin Login page'''
        assert admin_page.check_find_quote is True

    def test_admin_portal_004(self,admin_page):
        '''Verify the Find Address in Admin Login page'''
        assert admin_page.check_find_address is True

    def test_admin_portal_005(self,admin_page):
        '''Verify the Find Client in Admin Login page'''
        assert admin_page.check_find_client is True

    def test_admin_portal_006(self,admin_page):
        '''Verify the Copyright and Terms'''
        copyright_, terms = admin_page.check_copyright
        assert "2025" in copyright_ or "©" in copyright_
        assert "Terms" in terms