from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class Test_Odev(unittest.TestCase):
    def test_empty_username(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userNameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)
        userNameInput.send_keys("")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        #print(errorMessage.text)
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU:  {testResult}")

    def test_empty_password(self):
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            sleep(2)
            userNameInput = driver.find_element(By.ID, "user-name")
            passwordInput = driver.find_element(By.ID, "password")
            sleep(2)
            userNameInput.send_keys("standard_user")
            passwordInput.send_keys("")
            sleep(2)
            loginButton = driver.find_element(By.ID, "login-button")
            loginButton.click()
            sleep(2)
            errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
            #print(errorMessage.text)
            testResult = errorMessage.text == "Epic sadface: Password is required"
            print(f"TEST SONUCU:  {testResult}")

    def test_lockout_user(self):
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            sleep(2)
            userNameInput = driver.find_element(By.ID, "user-name")
            passwordInput = driver.find_element(By.ID, "password")
            sleep(2)
            userNameInput.send_keys("locked_out_user")
            passwordInput.send_keys("secret_sauce")
            sleep(2)
            loginButton = driver.find_element(By.ID, "login-button")
            loginButton.click()
            sleep(2)
            errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
            #print(errorMessage.text)
            testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
            print(f"TEST SONUCU:  {testResult}")

    def test_standard_user(self):
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get("https://www.saucedemo.com/")
            sleep(2)
            userNameInput = driver.find_element(By.ID, "user-name")
            passwordInput = driver.find_element(By.ID, "password")
            sleep(2)
            userNameInput.send_keys("standard_user")
            passwordInput.send_keys("secret_sauce")
            sleep(2)
            loginButton = driver.find_element(By.ID, "login-button")
            loginButton.click()
            sleep(2)
            expectedURL = "https://www.saucedemo.com/inventory.html"
            actualURL = driver.current_url
            self.assertEqual(expectedURL, actualURL)
            listOfItems = driver.find_elements(By.CLASS_NAME, "inventory_item")
            print(f"Saucedemo sitesinde şu an {len(listOfItems)} adet ürün bulunmaktadır.")
            
