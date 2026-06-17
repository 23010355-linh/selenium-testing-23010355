from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("123456")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

assert "Your username is invalid!" in driver.page_source

print("TC02 - Login Failed: PASS")

time.sleep(2)
driver.quit()
