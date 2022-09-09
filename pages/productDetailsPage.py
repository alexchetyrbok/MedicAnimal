import time
from pages.basePage import BasePage
from pages.locators import ProducDetailsPageLocators

class ProductDetailsPage(BasePage):

    def select_buy_option(self, option):
        time.sleep(5)
        self.click_radio(*ProducDetailsPageLocators.isRepeatFrequency, "OneOFF")