from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_Odev_2():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()

    def getData():
        return [("0","0"),("abc","123"),("tobeto","secret_sauce"),("standard_user","tobeto")]
    
    def getData_2():
        return [("standard_user",""),("locked_out_user",""),("problem_user",""),("performance_glitch_user","")]
    
    def test_empty_username(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username is required", "Error message is not as expected"

    @pytest.mark.parametrize("username, password", getData_2())
    def test_empty_password(self, username, password):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Password is required", "Error message is not as expected"


    def test_lockout_user(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"lockout_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out.", "Error message is not as expected"


    def test_standard_user(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        WebDriverWait(self.driver, 10).until(ec.url_to_be("https://www.saucedemo.com/inventory.html"))
        listOfItems = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        print(f"Saucedemo sitesinde şu an {len(listOfItems)} adet ürün bulunmaktadır.")


    @pytest.mark.parametrize("username, password", getData())
    def test_invalid_login(self, username, password):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        userNameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service", "Error message is not as expected"


    def test_add_to_cart(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addToCart = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()
        shopping_cart_badge = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a/span")))
        assert shopping_cart_badge.text == "1"

    def test_remove(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addToCart = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()
        removeButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
        assert removeButton.text == "Remove"
        removeButton.click()
        addToCart = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        assert addToCart.text == "Add to cart"


    def test_checkout(self):
        userNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput =WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"password")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()
        addToCart = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        addToCart.click()
        shoppingCartButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        shoppingCartButton.click()
        title_1 = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert title_1.text == "Your Cart"
        checkoutButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"checkout")))
        checkoutButton.click()
        title_2 = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert title_2.text == "Checkout: Your Information"
        firstNameInput = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"first-name")))
        lastNameInput =WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"last-name")))
        postalCodeInput =WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"postal-code")))
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(firstNameInput,"1")
        actions.send_keys_to_element(lastNameInput,"1")
        actions.send_keys_to_element(postalCodeInput,"1")
        actions.perform()
        continueButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"continue")))
        continueButton.click()
        title_3 = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert title_3.text == "Checkout: Overview"
        finishButton = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.ID,"finish")))
        finishButton.click()
        thanksMessage = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert thanksMessage.text == "Thank you for your order!"

