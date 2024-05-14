import time

from selenium.webdriver.common.by import By

from base.GetElements import Get


class TensorPage(Get):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    strength_in_people = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    about = (By.XPATH, '//a[@href="/about"][text()="Подробнее"]')

    # Action

    def click_about(self):
        self.get_element(self.about).click()





    # Method
    def go_to_about(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(self.strength_in_people))
        self.assert_word(word=self.get_element(self.strength_in_people).text, result='Сила в людях', text='Текст верен')
        self.click_about()
        self.assert_url('https://tensor.ru/about')



