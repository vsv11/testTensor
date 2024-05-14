

from selenium.webdriver.common.by import By

from base.GetElements import Get
from utilities.logger import Logger


class SbisPage(Get):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    button_contacts = (By.XPATH, '//a[@href="/contacts"]')

    # Action
    def click_contacts(self):
        self.get_element(self.button_contacts).click()
        print('Нажали на контакты')


    # Method
    def following_a_link(self):
        Logger.add_start_step(method='following_a_link')
        self.click_contacts()
        self.get_current_url()
        Logger.add_end_step(url=self.driver.current_url, method='following_a_link')
