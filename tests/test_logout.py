from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestLogout:
    def test_logout_by_exit_button(self, profile_driver):
        profile_driver.find_element(*Locators.user_screen_logout_button).click()

        WebDriverWait(profile_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.login_screen_title))
        assert profile_driver.find_element(*Locators.login_screen_title).is_displayed()
