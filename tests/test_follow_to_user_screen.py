from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from user import User


class TestFollowToUserScreen:
    user = User()

    def test_follow_by_app_header_user_account_link(self, driver):
        driver.get(Constants.BASE_URL + 'login')

        driver.find_element(*Locators.login_screen_email_input).send_keys(self.user.get_email())
        driver.find_element(*Locators.login_screen_password_input).send_keys(self.user.get_password())
        driver.find_element(*Locators.login_screen_submit_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.main_screen_title))
        driver.find_element(*Locators.app_header_enter_link).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.user_screen_title))
        assert driver.find_element(*Locators.user_screen_title).is_displayed()