# Author: Yi Sun(Tim) 2024-06-16

import pytest
import os
from selenium import webdriver
from UIModule.add_quote import Add_Quote
from UIModule.admin_portal import AdminPage
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
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://xxxx/")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def add_quote(driver,credentials):
    add_quote = Add_Quote(driver)
    add_quote.typeUserName(credentials["admin_username"])
    add_quote.typePassword(credentials["admin_password"])
    add_quote.clickLogin()
    add_quote.go_addquote()
    return add_quote



