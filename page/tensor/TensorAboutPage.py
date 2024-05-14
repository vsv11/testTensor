from selenium.webdriver.common.by import By

from base.GetElements import Get


class TensorAboutPage(Get):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    working = (By.XPATH, '//h2[text()="Работаем"]')
    img_1 = (By.XPATH, '//img[@alt="Разрабатываем систему СБИС"]')
    img_2 = (By.XPATH, '//img[@alt="Продвигаем сервисы"]')
    img_3 = (By.XPATH, '//img[@alt="Создаем инфраструктуру"]')
    img_4 = (By.XPATH, '//img[@alt="Сопровождаем клиентов"]')

    # Action

    def info_img_1(self):
        element = self.get_element(self.img_1)
        width = int(element.get_attribute('width'))
        height = int(element.get_attribute('height'))
        return {'width': width, 'height': height}

    def info_img_2(self):
        element = self.get_element(self.img_2)
        width = int(element.get_attribute('width'))
        height = int(element.get_attribute('height'))
        return {'width': width, 'height': height}

    def info_img_3(self):
        element = self.get_element(self.img_3)
        width = int(element.get_attribute('width'))
        height = int(element.get_attribute('height'))
        return {'width': width, 'height': height}

    def info_img_4(self):
        element = self.get_element(self.img_4)
        width = int(element.get_attribute('width'))
        height = int(element.get_attribute('height'))
        return {'width': width, 'height': height}



    # Method

    def comparison_img(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_element(self.working))
        if self.info_img_1() == self.info_img_2() == self.info_img_3() == self.info_img_4():
            print('Ширина и высота фотографий равны')
        else:
            print('Ширина и высота различается')

