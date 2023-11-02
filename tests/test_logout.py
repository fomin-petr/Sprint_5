from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, PrivatePageLocators


class TestLogout:
    def test_logout(self, registration, login, random_email, random_password):
        driver = login
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PrivatePageLocators.NAME_FIELD)))
        driver.find_element(By.XPATH, PrivatePageLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
