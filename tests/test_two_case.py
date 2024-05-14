import time

from page.sbis.SbisContactPage import SbisContactPage
from page.sbis.SbisPage import SbisPage


def test_two_case(setup_driver):
    driver = setup_driver
    sp = SbisPage(driver)
    sp.following_a_link()

    contact_link = SbisContactPage(driver)
    time.sleep(2)
    contact_link.contact()
