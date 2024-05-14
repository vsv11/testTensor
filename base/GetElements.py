from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.BaseClass import Base


class Get(Base):

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, TimeoutException)

    def get_element(self, locators):
        return (WebDriverWait(self.driver, 10, ignored_exceptions=self.ignored_exceptions)
                .until(EC.presence_of_element_located(locators)))
