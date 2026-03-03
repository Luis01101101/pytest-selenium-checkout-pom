from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self):
        self.browser = conftest.browser
        self.titulo_pagina = (By.XPATH, "//*[@class='app_logo']")
        self.item_inventario = (By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)