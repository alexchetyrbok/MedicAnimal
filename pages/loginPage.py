import random
import time

import pytest

from .basePage import BasePage
from selenium.webdriver.common.by import By
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def login(self, user_id):
        self.send_keys_to_editbox(LoginPageLocators.validateEmail, user_id, "Email")
        self.click_button(LoginPageLocators.validateEmailButton, "Continue")
        self.send_keys_to_editbox(LoginPageLocators.passwordLogin, "AChetyrbok12", "Password")
        self.click_button(LoginPageLocators.loginAndCheckoutButton, "Sign In")

    def sign_up(self):
        username = "testuser+" + str(time.time()) + "@gmail.com"
        self.send_keys_to_editbox(LoginPageLocators.validateEmail, username, "Email")
        self.click_button(LoginPageLocators.validateEmailButton, "Continue")
        time.sleep(1)
        self.send_keys_to_editbox(LoginPageLocators.PasswordLocator, "AChetyrbok12", "Password")
        self.select_dropdown(LoginPageLocators.TitleLocator, "mr")
        self.send_keys_to_editbox(LoginPageLocators.FullNameLocator, "test User", "Name")
        time.sleep(1)
        return username

