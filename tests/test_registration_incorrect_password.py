from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import locators
from constants import default_url
from user import User

driver = webdriver.Chrome()
driver.get(default_url)

driver.find_element(By.XPATH, locators.main_screen_enter_button).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_screen_title)))

driver.find_element(By.LINK_TEXT, locators.login_screen_register_link_text).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.register_screen_title)))
user = User()
driver.find_element(By.XPATH, locators.register_screen_name_input).send_keys(user.get_name())
driver.find_element(By.XPATH, locators.register_screen_email_input).send_keys(user.get_email())
driver.find_element(By.XPATH, locators.register_screen_password_input).send_keys('1')
driver.find_element(By.XPATH, locators.register_screen_submit_button).click()

assert driver.find_element(By.XPATH, f"{locators.register_screen_password_input}/parent::*/following-sibling::p[contains(@class, 'input__error')]").text == "Некорректный пароль"

driver.quit()