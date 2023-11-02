from selenium.webdriver.common.by import By
from locators import StartPageLocators


class TestSwitchConstructorTabs:
    def test_switch_to_sauce(self, start_page):
        driver = start_page
        sauce_button_class = driver.find_element(By.XPATH, StartPageLocators.SAUCE_TAB).get_attribute('class')
        driver.find_element(By.XPATH, StartPageLocators.SAUCE_TAB).click()
        assert driver.find_element(By.XPATH, StartPageLocators.SAUCE_TAB).get_attribute('class') != sauce_button_class

    def test_switch_to_ingredients(self, start_page):
        driver = start_page
        ingredients_button_class = driver.find_element(By.XPATH, StartPageLocators.INGREDIENTS_TAB).get_attribute('class')
        driver.find_element(By.XPATH, StartPageLocators.INGREDIENTS_TAB).click()
        assert driver.find_element(By.XPATH, StartPageLocators.INGREDIENTS_TAB).get_attribute('class') != ingredients_button_class

    def test_switch_to_buns(self, start_page):
        driver = start_page
        buns_button_class = driver.find_element(By.XPATH, StartPageLocators.BUN_TAB).get_attribute('class')
        driver.find_element(By.XPATH, StartPageLocators.SAUCE_TAB).click()
        driver.find_element(By.XPATH, StartPageLocators.BUN_TAB).click()
        assert driver.find_element(By.XPATH, StartPageLocators.BUN_TAB).get_attribute('class') == buns_button_class
