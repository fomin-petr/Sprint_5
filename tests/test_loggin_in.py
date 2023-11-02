from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordPageLocators


class TestLogin:
    def test_login_in_main_page(self, registration, start_page, random_email, random_password):
        driver = start_page
        driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
        driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_by_click_private_page(self, registration, start_page, random_email, random_password):
        driver = start_page
        driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
        driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_registration_page(self, registration, start_page, random_email, random_password):
        driver = start_page
        driver.find_element(By.XPATH, StartPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, RegistrationPageLocators.NAME_INPUT_FIELD)))
        driver.find_element(By.XPATH, RegistrationPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
        driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_password_recovery(self, registration, start_page, random_email, random_password):
        driver = start_page
        driver.find_element(By.XPATH, StartPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.FORGOT_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ForgotPasswordPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, ForgotPasswordPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
        driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.CREATE_ORDER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
