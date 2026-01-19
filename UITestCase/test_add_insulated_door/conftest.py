# Author:Yi Sun(Tim) 2023-9-16

import pytest
import os
from UIModule.add_insulated_door import Add_Insulated_Door
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
def add_insulated_door(driver,credentials):
    add_insulated_door = Add_Insulated_Door(driver)
    add_insulated_door.typeUserName(credentials["admin_username"])
    add_insulated_door.typePassword(credentials["admin_password"])
    add_insulated_door.clickLogin()
    add_insulated_door.go_addquote()
    add_insulated_door.go_addstandarddoor()
    add_insulated_door.add_insulated_door()
    return add_insulated_door