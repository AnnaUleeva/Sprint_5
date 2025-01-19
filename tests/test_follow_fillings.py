import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import default_url

import locators

driver = webdriver.Chrome()
driver.get(default_url)

driver.find_element(By.XPATH, locators.main_screen_fillings_tab).click()
time.sleep(1)
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.main_screen_fillings_title)))

driver.quit()