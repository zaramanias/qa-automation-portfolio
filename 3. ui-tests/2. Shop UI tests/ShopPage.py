
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class ShopPage:
    """
    PageObject: главная страница и каталог магазина saucedemo.com
    """
    def __init__(self, driver):
        """
        Инициализация страницы магазина.
        :param driver: WebDriver - экземпляр Selenium WebDriver
        :return: None
        """
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10, 0.01)

    @allure.step("Переход на страницу магазина")
    def open(self):
        """
        Переходит на страницу магазина
        :return: None
        """
        self.driver.get("https://www.saucedemo.com")

    @allure.step("""Авторизация в магазине с такими данными
                 {username}:{password} и нажатие кнопки 'Login'""")
    def login(self, username: str, password: str) -> None:
        """
        Авторизуется в магазине и переходит в каталог
        :param username: str - логин пользователя
        :param password: str - пароль пользователя
        :return: None
        """
        self.waiter.until(EC.visibility_of_element_located((
            By.ID, "user-name"))).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step(
            "Добавление в корзину 3 товаров: backpack, bolt t-shirt, onesie")
    def add_to_cart(self):
        """
        Добавляет в корзину 3 товара:
        Sauce labs backpack
        Sauce labs bolt t-shirt
        Sauce labs onesie
        """
        self.waiter.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()
