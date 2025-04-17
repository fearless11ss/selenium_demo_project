from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    select_product1 = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    select_product2 = '//*[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product3 = '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//*[@id="shopping_cart_container"]/a'
    menu_button = '//*[@id="react-burger-menu-btn"]'
    about_button = '//*[@id="about_sidebar_link"]'

    # Getters
    def get_product1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product1)))
    def get_product2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product2)))
    def get_product3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product3)))
    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))
    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))
    
    
    # Actions
    def click_select_product1(self):
        self.get_product1().click()
        print("Click select_product1")
    def click_select_product2(self):
        self.get_product2().click()
        print("Click select_product2")
    def click_select_product3(self):
        self.get_product3().click()
        print("Click select_product3")
    def click_get_cart(self):
        self.get_cart().click()
        print("Click get_cart")
    def click_menu_button(self):
        self.get_menu_button().click()
        print("Click menu_button")
    def click_about_button(self):
        self.get_about_button().click()
        print("Click about_button")


    # Methods
    def select_products1(self):
        self.get_current_url()
        self.click_select_product1()
        self.click_get_cart()
    def select_products2(self):
        self.get_current_url()
        self.click_select_product2()
        self.click_get_cart()
    def select_products3(self):
        self.get_current_url()
        self.click_select_product3()
        self.click_get_cart()
    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.assert_url('https://saucelabs.com/')