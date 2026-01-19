# Author: Yi Sun(Tim) 2023-08-29

'''Admin Page - Pytest Version'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UIModule.login_admin import Admin_Portal


class AdminPage(Admin_Portal):

    '''loc for default values in this page'''
    eco_icon_loc = (By.XPATH,'/html/body/div[2]/div/div[1]/a/img')
    add_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/ul/li[1]/a')
    list_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/ul/li[2]/a')
    findquote_box_loc = (By.ID,'search-quote')
    findquote_button_loc= (By.ID, 'btnFindQuote')
    findaddress_box_loc = (By.ID,'search-address')
    findaddress_button_loc= (By.ID, 'btnFindAddress')
    findclient_box_loc = (By.ID,'search-client')
    findclient_button_loc= (By.ID, 'btnFindClient')

    account_loc = (By.CSS_SELECTOR, "[aria-label='account']")
    copyright_loc = (By.CSS_SELECTOR, "[aria-label='copyright']")
    terms_loc = (By.CSS_SELECTOR, "[aria-label='terms']")

    '''Add Menu'''
    quote_add_loc = (By.CSS_SELECTOR,"[aria-label='quote_add']")
    lead_add_loc = (By.CSS_SELECTOR,"[aria-label='lead_add']")
    account_add_loc = (By.CSS_SELECTOR,"[aria-label='account_add']")
    installer_add_loc = (By.CSS_SELECTOR,"[aria-label='installer_add']")

    '''List Menu'''
    quote_list_loc = (By.ID,'quotelist)')
    services_list_loc = (By.ID,'servicelist')
    account_list_loc = (By.ID,'accountlist')
    report_list_loc = (By.ID,'reportlist)
    installer_list_loc = (By.ID,'installerlist')
    myob_list_loc = (By.ID,'myoblist')
    jobaccept_list_loc = (By.ID,'jobacceptlist')
    onhold_list_loc = (By.ID,'onholdlist')
    neworder_list_loc = (By.ID,'neworderlist')
    production_list_loc = (By.ID,'productionlist')
    productionWA_list_loc = (By.ID, 'walist')
    schedule_list_loc = (By.ID,'schedulelist')
    pipeline_list_loc = (By.ID,'pipelinelist')
    activepipeline_list_loc = (By.ID, 'activepipelinelist')

    '''Account Menu'''
    changepwd_loc = (By.ID,'pwdchange')
    updateprofile_loc = (By.ID,'profileupdate)
    updateemail_loc = (By.ID, 'emailupdate')
    usermanage_loc = (By.ID, 'usermanager')
    travel_area_loc = (By.ID,'travelarea')
    rollcycle_loc = (By.ID 'rollcycle')
    rollcycle_panellift_loc = (By.ID,'rollcyclepanel')
    rollcycle_rollerdoors_loc = (By.ID,'rollcycleroll')
    rollcycle_optiliftdoors_loc = (By.ID,'rollcycleoptilift')
    rollcycle_optirolldoors_loc = (By.ID, 'rollcycleoptiroll')
    sms_loc = (By.ID,'sms')
    logoff_loc = (By.ID, 'logoff')

    @property
    def get_url(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.copyright_loc)
        )
        print(self.driver.current_url)
        return self.driver.current_url

    @property
    def check_default_menu(self):
        return (
            self.driver.find_element(*self.add_loc).text,
            self.driver.find_element(*self.list_loc).text,
            self.driver.find_element(*self.account_loc).text,
        )

    @property
    def check_find_quote(self):
        return self.driver.find_element(*self.findquote_box_loc).is_displayed()

    @property
    def check_find_address(self):
        return self.driver.find_element(*self.findaddress_box_loc).is_displayed()

    @property
    def check_find_client(self):
        return self.driver.find_element(*self.findclient_box_loc).is_displayed()

    @property
    def check_copyright(self):
        return (
            self.driver.find_element(*self.copyright_loc).text,
            self.driver.find_element(*self.terms_loc).text
        )

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://xxxxx.com/")
    page = AdminPage(driver)
    page.typeUserName('xx@xx.com.au')
    page.typePassword('xxxxx')
    page.clickLogin()
    page.get_url  # 只测试这一个功能
    driver.quit()