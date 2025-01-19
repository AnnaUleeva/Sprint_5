from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import default_url

import locators

driver = webdriver.Chrome()
driver.get(default_url)

driver.find_element(By.XPATH, locators.app_header_enter_link).click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.login_screen_title)))

assert driver.find_element(By.XPATH, locators.login_screen_title).text == 'Вход'

driver.quit()