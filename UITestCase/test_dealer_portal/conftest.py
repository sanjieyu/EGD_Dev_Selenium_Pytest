# Author: Yi Sun(Tim) 2024-01-19

import pytest
import os
from UIModule.dealer_portal import Deal_Portal
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
def dealer_portal(driver,credentials):
    dealer_portal = Deal_Portal(driver)
    dealer_portal.typeUserName(credentials["dealer_username"])
    dealer_portal.typePassword(credentials["dealer_password"])
    dealer_portal.clickLogin()
    return dealer_portal



