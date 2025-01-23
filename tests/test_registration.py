from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from user import User

class TestRegistration:
    register_url = Constants.BASE_URL + 'register'

    def test_registration_incorrect_password(self, driver):
        driver.get(self.register_url)
        user = User()

        driver.find_element(*Locators.register_screen_name_input).send_keys(user.get_name())
        driver.find_element(*Locators.register_screen_email_input).send_keys(user.get_email())
        driver.find_element(*Locators.register_screen_password_input).send_keys('1')
        driver.find_element(*Locators.register_screen_submit_button).click()

        assert driver.find_element(*Locators.register_screen_password_input_error).text == "Некорректный пароль"

    def test_registration_success(self, driver):
        driver.get(self.register_url)
        user = User()
        user.create_random_email()

        driver.find_element(*Locators.register_screen_name_input).send_keys(user.get_name())
        driver.find_element(*Locators.register_screen_email_input).send_keys(user.get_email())
        driver.find_element(*Locators.register_screen_password_input).send_keys(user.get_password())
        driver.find_element(*Locators.register_screen_submit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_screen_title))
        driver.find_element(*Locators.login_screen_email_input).send_keys(user.get_email())
        driver.find_element(*Locators.login_screen_password_input).send_keys(user.get_password())
        driver.find_element(*Locators.login_screen_submit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.main_screen_title))
        assert driver.find_element(*Locators.main_screen_checkout_button).is_displayed()