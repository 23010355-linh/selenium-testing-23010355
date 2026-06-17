from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").click()

assert "You logged out of the secure area!" in driver.page_source

print("TC03 - Logout Success: PASS")

time.sleep(2)
driver.quit()
