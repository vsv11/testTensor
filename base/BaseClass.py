
class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    def assert_url(self, result):
        url = self.driver.current_url
        assert url == result, 'Url does not match'

    def assert_word(self, word, result, text):
        value_word = word
        assert value_word == result, 'Word does not match'
        print(text)
