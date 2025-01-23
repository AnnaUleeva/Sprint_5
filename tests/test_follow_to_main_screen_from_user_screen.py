from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators

class TestFollowToMainScreenFromUserScreen:
    @staticmethod
    def check_main_screen(my_driver):
        WebDriverWait(my_driver, 3).until(expected_conditions.visibility_of_element_located(Locators.main_screen_title))
        assert my_driver.current_url == Constants.BASE_URL


    def test_follow_by_constructor(self, profile_driver):
        profile_driver.find_element(*Locators.app_header_constructor).click()
        self.check_main_screen(profile_driver)

    def test_follow_by_logo(self, profile_driver):
        profile_driver.find_element(*Locators.app_header_logo).click()
        self.check_main_screen(profile_driver)