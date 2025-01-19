from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import default_url
from user import User

import locators

driver = webdriver.Chrome()
driver.get(default_url)

user = User()

driver.find_element(By.XPATH, locators.app_header_enter_link).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_screen_title)))

driver.find_element(By.XPATH, locators.login_screen_email_input).send_keys(user.get_email())
driver.find_element(By.XPATH, locators.login_screen_password_input).send_keys(user.get_password())
driver.find_element(By.XPATH, locators.login_screen_submit_button).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.main_screen_title)))
driver.find_element(By.XPATH, locators.app_header_enter_link).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.user_screen_title)))
driver.find_element(By.XPATH, locators.app_header_constructor).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.main_screen_title)))
assert driver.current_url == default_url

driver.quit()