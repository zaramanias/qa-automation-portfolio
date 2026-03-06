
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """
    Page Object: страница корзины и оформления заказа saucedemo.com
    """
    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины
        :param driver: WebDriver - экземпляр Selenium WebDriver
        :return: None
        """
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10, 0.01)

    @allure.step("Переход на страницу корзины")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины
        :return: None
        """
        self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Нажатие кнопки 'Checkout'")
    def checkout(self):
        """
        Нажимает кнопку Checkout и переходит к вводу данных покупателя
        :return: None
        """
        self.waiter.until(EC.element_to_be_clickable((
            By.ID, "checkout"))).click()

    @allure.step("""Заполнение данных на странице оформленя закаказа
                 этими данными {first_name}, {last_name}, {postal_code}""")
    def fill_checkout_info(self, first_name: str, last_name: str,
                           postal_code: str) -> None:
        """
        Заполняет данные на странице оформления заказа и переходит
        на шаг с итоговой суммой.
        :param first_name: str - Имя
        :param last_name: str - Фамилия
        :param postal_code: str - Почтовый индекс
        :return: None
        """
        self.waiter.until(EC.visibility_of_element_located((
            By.ID, "first-name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

        # Ждем появяления блока с итоговой суммой
        self.waiter.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label")))

    @allure.step("Получение итоговой суммы")
    def get_result(self) -> str:
        """
        Возвращает текст итоговой суммы (Total)
        :return: str - строка вида 'Total: $58.29'.
        """
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
