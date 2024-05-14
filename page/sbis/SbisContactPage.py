import time

from selenium.webdriver.common.by import By

from base.GetElements import Get


class SbisContactPage(Get):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    obl = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    city = (By.XPATH, '//div[@id="city-id-2"]')
    kamchatskiy_kray = (By.XPATH, './/li[@tabindex][43]')

    #Action
    def text_obl(self):
        self.driver.find_element(self.obl).text()
        print('Получили текст области')

    def text_city(self):
        self.driver.find_element(self.city).text()
        print('Получили текст ')

    def click_obl(self):
        self.get_element(self.obl).click()
        print('Нажали на область')

    def click_kamchatskiy_kray(self):
        self.get_element(self.kamchatskiy_kray).click()


    def contact(self):
        self.assert_word(word=self.get_element(self.obl).text, result='Свердловская обл.', text='Регион Свердловская обл.')
        self.assert_word(word=self.get_element(self.city).text, result='Екатеринбург', text='Город Екатеринбург')
        self.click_obl()
        self.click_kamchatskiy_kray()
        time.sleep(2)
        self.assert_word(word=self.get_element(self.obl).text, result='Камчатский край', text='Камчатский край')
        self.assert_word(word=self.get_element(self.city).text, result='Петропавловск-Камчатский', text='Город Петропавловск-Камчатский')
        self.assert_word(word=self.driver.title[16:], result='Камчатский край', text='В titile регион Камчатский край')
        url = self.driver.current_url
        if '41-kamchatskij-kraj' in url:
            print('Данные в URL верны')
        else:
            print('URL не верен')





