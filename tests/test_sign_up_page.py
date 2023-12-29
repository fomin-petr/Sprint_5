from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, RegistrationPageLocators, PrivatePageLocators
from CommonFunctions import Helper


class TestRegistration:
    def test_successful_registration(self, start_page):
        driver = start_page
        email = Helper.email_randomizer()
        password = Helper.password_randomizer()
        driver.find_element(By.XPATH, StartPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, RegistrationPageLocators.NAME_INPUT_FIELD)))
        driver.find_element(By.XPATH, RegistrationPageLocators.NAME_INPUT_FIELD).send_keys('Test')
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(By.XPATH, RegistrationPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON)))
        driver.find_element(By.XPATH, StartPageLocators.PRIVATE_PAGE_BUTTON).click()
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located((By.XPATH, PrivatePageLocators.NAME_FIELD)))
        tested_name = driver.find_element(By.XPATH, PrivatePageLocators.NAME_FIELD)
        tested_email = driver.find_element(By.XPATH, PrivatePageLocators.LOGIN_FIELD)
        assert tested_name.get_attribute('value') == 'Test'
        assert tested_email.get_attribute('value') == email.lower()

    def test_registration_password_less_6_chars_fail(self, start_page, random_email):
        email = random_email
        driver = start_page
        driver.find_element(By.XPATH, StartPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.REGISTRATION_BUTTON)))
        driver.find_element(By.XPATH, LoginPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, RegistrationPageLocators.NAME_INPUT_FIELD)))
        driver.find_element(By.XPATH, RegistrationPageLocators.NAME_INPUT_FIELD).send_keys('Test')
        driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_INPUT_FIELD).send_keys(email)
        driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_INPUT_FIELD).send_keys('12345')
        driver.find_element(By.XPATH, RegistrationPageLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, RegistrationPageLocators.ERROR_MESSAGE)))
        assert driver.find_element(By.XPATH, RegistrationPageLocators.ERROR_MESSAGE).text == "Некорректный пароль"
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
