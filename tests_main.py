import time
from selenium import webdriver

from pages.mainPage import MainPage
from pages.loginPage import LoginPage
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
def test_login(browser, link, fixure2):
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
   # page.open()  # открываем страницу
   # page.accept_cookies()
   # page.sign_up()
    print(fixure2)
   # print(username)kkkjj
   # page.login("a.chetyrbok+11@gmail.com")
