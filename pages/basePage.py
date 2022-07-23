from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)
        print("Page" + self.url+ " was opened!")

    def accept_cookies(self):
        self.browser.find_element(By.ID, "onetrust-accept-btn-handler").click()
        print("Cookies were accepted")

    def send_keys_to_editbox(self, locator, value, fieldName):
        field = self.browser.find_element(*locator)
        field.send_keys(value)
        print("Value "+ value + " was set to the field " + fieldName)

    def click_button(self, locator, buttonName):
        button = self.browser.find_element(*locator)
        button.click()
        print("Button " + buttonName + " was clicked")

    def select_dropdown(self, locator, value):
        select = Select(self.browser.find_element(*locator))
        select.select_by_value(value)  # ищем элемент с текстом "Python"
        print("Value " + value + " selected in dropdown")
