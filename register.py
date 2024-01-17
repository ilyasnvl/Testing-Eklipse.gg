from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://eklipse.gg/")

def test_check_placeholder_register(): #TC010
    driver.find_element(By.LINK_TEXT, "Sign Up For Free").click()
    name_register = driver.find_element(By.CSS_SELECTOR, "#name").get_attribute("placeholder")
    email_register = driver.find_element(By.CSS_SELECTOR, "#email").get_attribute("placeholder")
    pass_register = driver.find_element(By.CSS_SELECTOR, "#password").get_attribute("placeholder")
    conf_pass_register = driver.find_element(By.CSS_SELECTOR, "#password_confirmation").get_attribute("placeholder")

    # verify text placeholder pada setiap field
    assert "Name" in name_register
    assert "Email Address" in email_register
    assert "Password" in pass_register
    assert "Confirm password" in conf_pass_register

def test_register_with_valid_data(): #TC011
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("ilyas nauval")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("ilyas04@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "#password_confirmation").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(5)
    
    # verify url after register
    assert "https://app.eklipse.gg/home" == driver.current_url

    driver.close() 

def test_register_with_already_data(): #TC012
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.eklipse.gg/register")  
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("ilyas")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("min170897@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Junaedi48")
    driver.find_element(By.CSS_SELECTOR, "#password_confirmation").send_keys("Junaedi48")
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    time.sleep(3)
    
    # verify error message ketika gagal register
    error_msg_regist = driver.find_element(By.CSS_SELECTOR, ".alert").text
    assert "The email has already been taken." in error_msg_regist
    time.sleep(2)

def test_doesnt_match_password(): #TC013
    driver.find_element(By.CSS_SELECTOR, "#name").clear()
    driver.find_element(By.CSS_SELECTOR, "#email").clear()
    driver.find_element(By.CSS_SELECTOR, "#password").clear()
    driver.find_element(By.CSS_SELECTOR, "#password_confirmation").clear()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Jaka")
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("jakabudiman@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "#password_confirmation").send_keys("password")
    time.sleep(2)

    # verify error message password tidak sama
    error_msg_pass = driver.find_element(By.CSS_SELECTOR, ".invalid-feedback").text
    assert "Password & Confirm Password does not match" in error_msg_pass
