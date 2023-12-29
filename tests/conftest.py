import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StartPageLocators, LoginPageLocators, RegistrationPageLocators
import random
from random import choice
from string import ascii_letters


@pytest.fixture()
def registration(start_page, random_email, random_password):
    email = random_email
    password = random_password
    driver = start_page
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
    driver.find_element(By.XPATH, StartPageLocators.LOGO_BUTTON).click()
    yield driver


@pytest.fixture()
def login(start_page, random_email, random_password):
    driver = start_page
    driver.find_element(By.XPATH, StartPageLocators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginPageLocators.LOGIN_BUTTON)))
    driver.find_element(By.XPATH, LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(random_email)
    driver.find_element(By.XPATH, LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(random_password)
    driver.find_element(By.XPATH, LoginPageLocators.LOGIN_BUTTON).click()
    yield driver


@pytest.fixture()
def start_page():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def random_email():
    random_email = ''
    for i in range(8):
        random_email += choice(ascii_letters)
    random_email += '__' + str(random.randint(0, 99999999)) + '@yaya.ru'
    return random_email


@pytest.fixture()
def random_password():
    random_password = random.randint(100000, 999999)
    return random_password
