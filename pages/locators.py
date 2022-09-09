from selenium.webdriver.common.by import By

class LoginPageLocators():
    validateEmail = (By.ID, "validateEmail")
    validateEmailButton = (By.XPATH, "//*[contains(@class, 'create-account-primary-button')]")
    TitleLocator = (By.ID, "registerTitle")
    FullNameLocator = (By.ID, "registerFullName")
    EmailLocator = (By.ID, "registerEmail")
    PasswordLocator = (By.NAME, "pwd")
    OptInLocator = (By.ID, "register.optInDisplay")
    RegisterButtonLocator = (By.ID, "createAccountButton")
    RegPageLocator = (By.XPATH, "/html/body")
    passwordLogin = (By.ID, "password")
    loginAndCheckoutButton = (By.ID, "loginAndCheckoutButton")
    recapcha = (By.CLASS_NAME, "recaptcha-checkbox-border")

class MyAccountPageLocators():
    WelcomeHeading = (By.CLASS_NAME, "welcome")

class ProductListingPageLocators():

    Productcard = (By.CSS_SELECTOR, "li[class ^=""product-item""]")

class ProducDetailsPageLocators():
        FrequencyDropLocator = (By.ID, "repeatFrequency")
        AddToCartLocator = (By.ID, "addToCartButton")
        isRepeatFrequency = (By.ID, "regular-option")
        oneTime = (By.ID, "one-time-option")