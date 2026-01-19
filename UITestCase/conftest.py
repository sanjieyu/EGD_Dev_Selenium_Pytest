# Author: Yi Sun(Tim) 2023-06-16

import pytest
import os
from pathlib import Path
from selenium import webdriver
from datetime import datetime
from CommonModule.read_config import ReadConfig


@pytest.fixture(scope="class")
def credentials():
    config_read = ReadConfig()
    return {
        "egd_url": config_read.get_url(),
        "admin_username": config_read.admin_username(),
        "admin_password": config_read.admin_password()
    }


@pytest.fixture(scope="class")
def driver(request, credentials):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(credentials["egd_url"])
    request.node.driver = driver
    yield driver
    driver.quit()