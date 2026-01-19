# Author:Yi Sun(Tim) 2023-4-16

import pytest
import os
from UIModule.standard_door import Standard_Door
from UITestCase.conftest import credentials,driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # 创建截图目录
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # 失败截图
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver and hasattr(driver, "save_screenshot"):
            driver.save_screenshot(f"screenshots/{item.name}.png")

@pytest.fixture(scope="class")
def standard_door(driver,credentials):
    standard_door = Standard_Door(driver)
    standard_door.typeUserName(credentials["admin_username"])
    standard_door.typePassword(credentials["admin_password"])
    standard_door.clickLogin()
    standard_door.go_addquote()
    standard_door.go_addstandarddoor()
    return standard_door