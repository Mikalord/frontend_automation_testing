# To-Dos:
# 1. Ivalid credentials display error message when both fiels are blank
# 2. Invalid credentials display error message when password is blank
# 3. Invalid credentials display error message when username is blank


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage:
    # Set up the driver
    @pytest.fixture
    def driver(self):
        # headless drivers are faster
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        yield driver
        driver.quit()

    # Test case 1: Login form is displayed
    def test_login_form_displayed(self, driver):
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")

        # Check that the login form is displayed
        login_box = driver.find_element(By.CLASS_NAME, "login-box")
        assert login_box.is_displayed()

    # Test case 2: Login form contains username and password fields
    def test_login_form_contains_fields(self, driver):
        # Navigate to the login page
        driver.get("https://www.saucedemo.com")

        # Check that the login form contains username and password fields
        username_field = driver.find_element(By.NAME, "user-name")
        password_field = driver.find_element(By.NAME, "password")
        assert username_field.is_displayed()
        assert password_field.is_displayed()

    # Test case 3: Login displays error message when password is blank
    def test_error_msg(self, driver):
        # Navigate to the login page
        driver.get("https://www.saucedemo.com")

        # Fill in the username field, but leave the password field blank
        username_field = driver.find_element(By.NAME, "user-name")
        username_field.send_keys("standard_user")

        # Click the login button
        login_button = driver.find_element(By.NAME, "login-button")
        login_button.click()

        # Check that the error message is displayed
        error_msg = driver.find_element(By.CLASS_NAME, "error-button")
        assert error_msg.is_displayed()

    # Test case 4: Login and redirected to home page when credentials are valid
    def test_login_button_enabled_when_complete(self, driver):
        # Navigate to the login page
        driver.get("https://www.saucedemo.com")

        # Fill in the username and password fields with valid credentials
        username_field = driver.find_element(By.NAME, "user-name")
        username_field.send_keys("standard_user")
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("secret_sauce")

        # Check that redir to home page is successful when credentials are valid
        login_button = driver.find_element(By.NAME, "login-button")
        login_button.click()
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
