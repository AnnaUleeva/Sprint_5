import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators import Locators
from user import User


@pytest.fixture # Возвращает драйвер
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture # Возвращает драйвер с авторизованным пользователем на странице профиля
def profile_driver():
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL + 'login')

    user = User()
    driver.find_element(*Locators.login_screen_email_input).send_keys(user.get_email())
    driver.find_element(*Locators.login_screen_password_input).send_keys(user.get_password())
    driver.find_element(*Locators.login_screen_submit_button).click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.main_screen_title))
    driver.find_element(*Locators.app_header_enter_link).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.user_screen_title))

    yield driver

    driver.quit()