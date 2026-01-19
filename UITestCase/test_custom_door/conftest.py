# Author:Yi Sun(Tim) 2023-4-16

import pytest
import os
# from selenium import webdriver
# from UIModule.admin_portal import AdminPage
# from CommonModule.read_config import ReadConfig
from UIModule.custom_door import Custom_Door
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
def custom_door(driver,credentials):
    custom_door = Custom_Door(driver)
    custom_door.typeUserName(credentials["admin_username"])
    custom_door.typePassword(credentials["admin_password"])
    custom_door.clickLogin()
    custom_door.go_addquote()
    custom_door.go_addcustomdoor()
    return custom_door