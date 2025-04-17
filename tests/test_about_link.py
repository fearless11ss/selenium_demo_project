from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
sys.path.append("C:\\Users\\Administrator\\Desktop\\Программирование\\selenium_project")
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.payment_page import Payment_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime


def test_about_link():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--incognito")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service('C:\\Users\\Administrator\\Desktop\\Программирование\\selenium_project\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    print("Start test")
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    