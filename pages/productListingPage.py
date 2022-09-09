import time

from .basePage import BasePage
from pages.locators import ProductListingPageLocators


class ProductListingPage(BasePage):
    def openProduct(self, num):
        products = self.get_list_of_products()
        if len(products) == 0:
            num = 0
        product = products[num]
        product.click()
        print("Product was opened")
        time.sleep(1)

    def get_list_of_products(self):
        products = self.browser.find_elements(*ProductListingPageLocators.Productcard)
        return products

    def get_count_of_products(self):
        products = self.browser.find_elements(*ProductListingPageLocators.Productcard)
        return len(products)