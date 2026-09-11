from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@text="Enter email"]'
    )

    PASSWORD_FIELD = (
        AppiumBy.XPATH,
        '//android.widget.EditText[@text="Enter password"]'
        

    )
    

    LOGIN_BUTTON = (
        AppiumBy.XPATH,
        '//android.widget.TextView[@text="Login"]'
    )

    def is_login_page_displayed(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.EMAIL_FIELD)
            )
            return self.driver.find_element(*self.EMAIL_FIELD).is_displayed()
        except Exception:
            return False

    def enter_email(self, email):
        self.click(self.EMAIL_FIELD)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.click(self.PASSWORD_FIELD)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.hide_keyboard()

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.driver.hide_keyboard()
        self.click_login()
