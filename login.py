from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://eklipse.gg/")

def test_check_placeholder_login(): # TC014
    driver.find_element(By.LINK_TEXT, "Sign In").click()
    email_input = driver.find_element(By.CSS_SELECTOR, "#username").get_attribute("placeholder")
    password_input = driver.find_element(By.CSS_SELECTOR, "#password").get_attribute("placeholder")
    
    # Verify text placeholder
    assert "Email Address" in email_input
    assert "Password" in password_input

    time.sleep(3)

def test_login_with_valid_data(): #TC015
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("min170897@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Junaedi48")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(2)

    # verify url after login
    assert "https://app.eklipse.gg/home" == driver.current_url
    time.sleep(2)

    driver.close()

def test_login_with_invalid_data(): #TC016
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.eklipse.gg/login")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("emailinvalid.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("passwordinvalid")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    # Verify Tampil Pop Up ketika gagal login
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swal2-popup")))
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".swal2-confirm").click()

