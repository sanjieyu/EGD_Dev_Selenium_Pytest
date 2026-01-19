# Author:Yi Sun(Tim) 2023-4-16

import pytest
from UIModule.admin_portal import AdminPage
from UITestCase.conftest import credentials,driver


@pytest.fixture(scope="class")
def admin_page(driver,credentials):
    page = AdminPage(driver)
    page.typeUserName(credentials["admin_username"])
    page.typePassword(credentials["admin_password"])
    page.clickLogin()
    return page