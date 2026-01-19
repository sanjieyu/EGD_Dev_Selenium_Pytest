# Author:Yi Sun(Tim) 2023-10-16

import pytest
import os
from UIModule.add_quote_with_custom_door import Add_Quote_With_CustomDoor
from UIModule.custom_door import *
from UIModule.add_custom_door import Add_Custom_Door
from UITestCase.conftest import credentials,driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver and hasattr(driver, "save_screenshot"):
            driver.save_screenshot(f"screenshots/{item.name}.png")

@pytest.fixture(scope="class")
def add_quote_with_customdoor(driver,credentials):
    add_quote_with_customdoor = Add_Quote_With_CustomDoor(driver)
    add_quote_with_customdoor.typeUserName(credentials["admin_username"])
    add_quote_with_customdoor.typePassword(credentials["admin_password"])
    add_quote_with_customdoor.clickLogin()
    add_quote_with_customdoor.add_custom_door_fun()
    add_quote_with_customdoor.get_proposal_number
    add_quote_with_customdoor.search_new_quote()
    return add_quote_with_customdoor