import time
from selenium.webdriver.common.by import By
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestLoginCompra:
    def test_login_compra(self):

        browser = conftest.browser
        home_page = HomePage()
        login_page = LoginPage()

        # login
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()

        #adicionar o produto no carrinho
        time.sleep(2)
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        #fazer o checkout
        home_page.acessar_carrinho()
        browser.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium checkout_button ']").click()
        time.sleep(2)
        browser.find_element(By.ID, "first-name").send_keys("luis")
        browser.find_element(By.ID, "last-name").send_keys("matos")
        browser.find_element(By.ID, "postal-code").send_keys("123456")
        browser.find_element(By.XPATH, "//*[@class='submit-button btn btn_primary cart_button btn_action']").click()
        time.sleep(2)
        browser.find_element(By.XPATH, "//*[@class='btn btn_action btn_medium cart_button']").click()
        time.sleep(2)