

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class AdminPortal:
    def __init__(self, driver):
        self.driver = driver
        self.username_loc = (By.XPATH, '//*[@id="Email"]')
        self.password_loc = (By.XPATH, '//*[@id="Password"]')
        self.login_loc = (By.XPATH, '//*[@id="loginForm"]/form/div[4]/div/input')
        self.loginError_loc = (By.XPATH, '//*[@id="loginForm"]/form/div[3]/span')  # Example locator
        self.forgetpwd_loc = (By.LINK_TEXT, 'Forgot your password?')
        self.forgetdescription_loc = (By.XPATH, '//p[@class="description"]')
        self.inputemail_loc = (By.XPATH, '//*[@id="Email"]')
        self.forgetsubmit_loc = (By.XPATH, '//*[@id="submit"]')
        self.wrongemailwaring_loc = (By.XPATH, '//*[@id="Email-error"]')
        self.passwordrequire_loc = (By.XPATH, '//*[@id="Password-error"]')

    def type_username(self, username):
        self.driver.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_loc).click()

    def login(self, username, password):
        self.type_username(username)
        self.type_password(password)
        self.click_login()

    def get_username_text(self):
        return self.driver.find_element(*self.username_loc).get_attribute("value")

    def get_login_error(self):
        return self.driver.find_element(*self.loginError_loc).text

    def click_forget(self):
        self.driver.find_element(*self.forgetpwd_loc).click()

    def get_forget_description(self):
        return self.driver.find_element(*self.forgetdescription_loc).text

    def submit_wrong_email(self):
        self.driver.find_element(*self.inputemail_loc).send_keys('ddd')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    def get_wrong_email_warning(self):
        return self.driver.find_element(*self.wrongemailwaring_loc).text

    def submit_username(self):
        self.driver.find_element(*self.inputemail_loc).send_keys('xxxx@itrazotracetech.com')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    def get_password_require_warning(self):
        return self.driver.find_element(*self.passwordrequire_loc).text


# --- Fixtures ---

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://xxxxx")
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def portal(driver):
    return AdminPortal(driver)


# --- Tests ---

def test_login_success(portal):
    portal.login('ysun@ecogaragedoors.com.au', 'Tims@123')
    assert "egd2.sighte.com" in portal.driver.current_url.lower()


def test_login_error_message(portal):
    portal.login('invaliduser', 'wrongpassword')
    error = portal.get_login_error()
    assert 'Invalid' in error or 'wrong' in error.lower()


def test_forget_password_flow(portal):
    portal.click_forget()
    description = portal.get_forget_description()
    assert 'password' in description.lower()


def test_wrong_email_warning(portal):
    portal.click_forget()
    portal.submit_wrong_email()
    warning = portal.get_wrong_email_warning()
    assert 'valid email' in warning.lower() or 'required' in warning.lower()


def test_password_requirement_warning(portal):
    portal.click_forget()
    portal.submit_username()
    warning = portal.get_password_require_warning()
    assert 'required' in warning.lower() or 'enter' in warning.lower()