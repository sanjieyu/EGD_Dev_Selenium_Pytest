# Author:Yi Sun(Tim) 2023-4-16

import pytest
import os
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
def add_custom_door(driver,credentials):
    add_custom_door = Add_Custom_Door(driver)
    add_custom_door.typeUserName(credentials["admin_username"])
    add_custom_door.typePassword(credentials["admin_password"])
    add_custom_door.clickLogin()
    add_custom_door.go_addquote()
    add_custom_door.go_addcustomdoor()
    return add_custom_door