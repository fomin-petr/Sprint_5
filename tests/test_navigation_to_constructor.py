from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, PrivatePageLocators


class TestNavigationToConstructor:
    def test_navigation_to_constructor_by_click_in_private_page(self, registration, start_page, random_email, random_password):
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
        driver.find_element(By.XPATH, StartPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_to_constructor_by_click_logo_in_private_page(self, registration, start_page, random_email, random_password):
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
        driver.find_element(By.XPATH, StartPageLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

