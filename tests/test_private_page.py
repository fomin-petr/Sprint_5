from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, PrivatePageLocators


def test_private_page_button_logged_in(registration, start_page, random_email, random_password):
    driver = start_page
    driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
    driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
    driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
    driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PrivatePageLocators.NAME_FIELD)))
    tested_name = driver.find_element(By.XPATH, PrivatePageLocators.NAME_FIELD)
    tested_email = driver.find_element(By.XPATH, PrivatePageLocators.LOGIN_FIELD)
    assert tested_name.get_attribute('value') == 'Test'
    assert tested_email.get_attribute('value') == random_email.lower()
    driver.quit()