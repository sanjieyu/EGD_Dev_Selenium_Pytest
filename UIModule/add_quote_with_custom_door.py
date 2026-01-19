# Author:Yi Sun(Tim) 2023-5-05

'''Add a Quote with a Custom  door function'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from UIModule.custom_door import *
from UIModule.add_custom_door import Add_Custom_Door

class Add_Quote_With_CustomDoor(Add_Custom_Door):

    proposal_number_loc = (By.ID,'ProposalNo')
    find_quote_input = (By.ID,'search-quote')
    find_quote_btn = (By.ID,'search-btn')

    searched_proposal_no_loc = (By.CSS_SELECTOR, "a.dark-text[href^='/Quote/Edit/']")
    searched_door_no_loc = (By.XPATH, "//span[text()='Door 1(A1)']")
    searched_door_status_loc = (By.XPATH, "//span[text()='Quote']")


    def __init__(self,driver):
        self.driver = driver
        self.add_quote = Add_Quote(self.driver)
        self.add_custom_door = Add_Custom_Door(self.driver)

    def add_custom_door_fun(self):
        self.add_quote.go_addquote()
        self.add_custom_door.go_addcustomdoor()
        self.add_custom_door.add_custom_detail()
        sleep(2)
        self.add_quote.check_add_quote_success

    @property
    def get_proposal_number(self):
        global proposal_number
        proposal_number = self.driver.find_element(*self.proposal_number_loc).get_attribute('value')
        print('number is:',proposal_number)
        return proposal_number

    def search_new_quote(self):
        self.driver.refresh()
        self.driver.find_element(*self.find_quote_input).send_keys(proposal_number)
        self.driver.find_element(*self.find_quote_btn).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searched_door_no_loc))

    @property
    def verify_new_quote(self):
        searched_proposal_no = self.driver.find_element(*self.searched_proposal_no_loc).text
        searched_door_no = self.driver.find_element(*self.searched_door_no_loc).text
        searched_door_status = self.driver.find_element(*self.searched_door_status_loc).text
        print(searched_door_no,searched_door_status)
        return searched_door_no,searched_door_status

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://xxxx/")
    page = Add_Quote_With_CustomDoor(driver)
    page.typeUserName('xx@xxx.com.au')
    page.typePassword('xxxxxx')
    page.clickLogin()
    page.add_custom_door_fun()
    page.get_proposal_number
    page.search_new_quote()
    page.verify_new_quote