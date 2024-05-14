from page.sbis.SbisPage import SbisPage
from page.tensor.TensorAboutPage import TensorAboutPage
from page.tensor.TensorPage import TensorPage


def test_one_case(setup_driver):
    driver = setup_driver
    SP = SbisPage(driver)
    SP.following_a_link()

    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get('https://tensor.ru/')

    TP = TensorPage(driver)
    TP.go_to_about()

    TAP = TensorAboutPage(driver)
    TAP.comparison_img()







