from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://eklipse.gg/")

def test_check_menu(): #TC001
    products_menu = driver.find_element(By.XPATH, "//a[.='Products']").text
    use_case_menu = driver.find_element(By.XPATH, "//li[contains(.,'Use Case')]").text
    discovery_menu = driver.find_element(By.XPATH, "//span[.='Discovery']").text
    premium_menu = driver.find_element(By.XPATH, "//a[.='Premium']").text

    # verify text pada setiap menu di navbar
    assert "PRODUCTS" in products_menu
    assert "USE CASE" in use_case_menu
    assert "DISCOVERY" in discovery_menu
    assert "PREMIUM" in premium_menu

def test_scroll_bottom_footer(): #TC002
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    footer_menu = driver.find_element(By.ID, "menu-footer-menu").text

    # verify menu pada footer
    assert "Help\nTerms\nPrivacy" in footer_menu
    time.sleep(3)

def test_check_text_copyright_footer(): #TC003
    footer_copyright = driver.find_element(By.CSS_SELECTOR, ".footer-copyright").text

    # verify text copyright pada footer
    assert "Copyright © 2023 Eklipse. All product names, logos, and brands are property of their respective owners. All company, product, visual and service names used in this website are for identification purposes only." in footer_copyright

def test_access_demo_page(): #TC004
    driver.execute_script("window.scrollTo(5, 5);")
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[.='demo page']").click()
    time.sleep(3)
    handles = driver.window_handles

    for handle in handles:
        driver.switch_to.window(handle)

    # verify url demo page
    assert "https://eklipse.gg/public-stream-demo" == driver.current_url

    