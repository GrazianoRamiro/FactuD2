from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class RPA:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )

    def navigate(self, url):
        self.driver.get(url)

    def find(self, tag, attr, value):
        xpath = f"//{tag}[@{attr}='{value}']"
        element = self.driver.find_element("xpath", xpath)

        if tag == "select":
            return Select(element)
        else:
            return element

    def find_and_click(self, tag, attr, value):
        element = self.find(tag, attr, value)
        element.click()
        self.wait(10)
        return

    def wait(self, time=100):
        return self.driver.implicitly_wait(time)

    def accept_alert(self):
        return self.driver.switch_to.alert.accept()
