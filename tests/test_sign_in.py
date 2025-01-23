import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from user import User


class TestSignIn:
    user = User()

    def fill_form_and_check(self, my_driver):
        WebDriverWait(my_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_screen_title))
        my_driver.find_element(*Locators.login_screen_email_input).send_keys(self.user.get_email())
        my_driver.find_element(*Locators.login_screen_password_input).send_keys(self.user.get_password())
        my_driver.find_element(*Locators.login_screen_submit_button).click()

        WebDriverWait(my_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.main_screen_title))
        assert my_driver.find_element(*Locators.main_screen_checkout_button).is_displayed()

    @pytest.mark.parametrize(
        'sign_in_locator',
        [
            Locators.app_header_enter_link,
            Locators.main_screen_enter_button
        ]
    )
    def test_sign_in_by_main_screen(self, driver, sign_in_locator):
        driver.get(Constants.BASE_URL)
        driver.find_element(*sign_in_locator).click()
        self.fill_form_and_check(driver)

    def test_sign_in_by_enter_link_in_register_screen(self, driver):
        driver.get(Constants.BASE_URL + 'register')
        driver.find_element(*Locators.register_screen_enter_link).click()
        self.fill_form_and_check(driver)

    def test_sign_in_by_enter_link_in_forgot_password(self, driver):
        driver.get(Constants.BASE_URL + 'forgot-password')
        driver.find_element(*Locators.forgot_password_screen_enter_link).click()
        self.fill_form_and_check(driver)