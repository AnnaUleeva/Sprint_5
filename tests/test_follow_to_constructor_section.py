import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import Locators


class TestFollowToConstructorSection:
    @pytest.mark.parametrize(
        'tab_locator, section_locator',
        [
            [Locators.main_screen_buns_tab, Locators.main_screen_buns_title],
            [Locators.main_screen_sauces_tab, Locators.main_screen_sauces_title],
            [Locators.main_screen_fillings_tab, Locators.main_screen_fillings_title]
        ]
    )
    def test_follow_to_constructor_section(self, driver, tab_locator, section_locator):
        driver.get(Constants.BASE_URL)
        driver.find_element(*tab_locator).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(section_locator))
        assert driver.find_element(*section_locator).is_displayed()

