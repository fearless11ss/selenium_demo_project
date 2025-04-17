import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    # get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    # check assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # take screenshot
    def take_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = 'screenshot'+now_date+'.png'
        self.driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\Программирование\\selenium_project\\screen\\'+screenshot_name)

    # assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url
        print("Good value url")