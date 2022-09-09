import random
import time
import pymssql

import requests as requests
from selenium import webdriver
from pages.locators import MyAccountPageLocators
from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from pages.productListingPage import ProductListingPage
from pages.productDetailsPage import ProductDetailsPage
import pytest
from selenium.webdriver.common.by import By

sites = ('link', ["https://medicanimal.com/login"])

#@pytest.mark.parametrize(*sites)
#def test_signup(browser, link):
#    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    page.open()  # открываем страницу
#    page.accept_cookies()
#    page.sign_up()

@pytest.mark.parametrize(*sites)
def test_login(browser, link):
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.accept_cookies()
    username = page.sign_up()
    page.login("a.chetyrbok+11@gmail.com")
    page.assert_meesage_contain_test(MyAccountPageLocators.WelcomeHeading, "Welcome Aleksey")

#№@pytest.mark.parametrize(*sites)
#def test_click_product(browser, link):
#    ListPage = ProductListingPage(browser, link+ "/Dog/c/c000001")  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#    ListPage.open()  # открываем страницу
#    ListPage.accept_cookies()
#    product_count_on_page = ListPage.get_count_of_products()
#    ListPage.openProduct(random.randrange(2, product_count_on_page-2, 1))
    #PDP = ProductDetailsPage(browser, "")
    #PDP.select_buy_option("OneOFF")

#def test_get_locations_for_us_90210_check_status_code_equals_200():
#    response = requests.get("http://api.zippopotam.us/us/90210")
#    requests.post()
#    assert response.status_code == 200
#    response_body = response.json()
#    print(response_body["country"])
