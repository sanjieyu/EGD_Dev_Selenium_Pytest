# Author: Yi Sun(Tim) 2023-08-05

import pytest
import os
from UIModule.account_customer import Account_Customer
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
def account_customer(driver,credentials):
    account_customer = Account_Customer(driver)
    account_customer.typeUserName(credentials["admin_username"])
    account_customer.typePassword(credentials["admin_password"])
    account_customer.clickLogin()
    account_customer.goto_account_customer()
    return account_customer