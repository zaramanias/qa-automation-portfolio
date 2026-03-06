
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        """
        Конструктор класса CalcPage
        :param driver:  WebDriver - объект драйвера Selenium.
        """
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 50, 0.01)
        self.first_number = None
        self.operator = None
        self.second_number = None

    @allure.step("Открытие страницы калькулятора")
    def open(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    @allure.step("Установка задержки {delay} секунд")
    def set_delay(self, delay):
        """
        Устанавливает задержку выполнения операции.
        :param delay: int время задержки в секундах
        """
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(delay)

    @allure.step("Нажатие кнопки '{symbol}'")
    def click_button(self, symbol):
        """
        Нажимает кнопку калькулятора по ее символу
        :param symbol: str - символ кнопки(цифра или оператор)
        :raise Exception: если кнопка не найдена
        """
        keys = self.driver.find_element(By.CSS_SELECTOR, "div.keys")
        buttons = keys.find_elements(By.TAG_NAME, "span")
        for button in buttons:
            if button.text == symbol:
                button.click()
                if symbol.isdigit():
                    if self.first_number is None:
                        self.first_number = symbol
                    else:
                        self.second_number = symbol
                if symbol in ['+', '-', 'x', '÷']:
                    self.operator = symbol

                return
        raise Exception(f"Button with symbol {symbol} not found")

    @allure.step("Ожидание исчезновения спиннера")
    def wait_spinner(self):
        """
        Ожидает исчезновения индикатора загрузки (spinner)
        """
        self.waiter.until(
            EC.invisibility_of_element_located((By.ID, "spinner")))

    @allure.step("Получение результата с экрана")
    def get_result(self):
        """
        Возвращает текст результата с экрана калькулятора.
        :return: str - результат вычесления
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text

    @allure.step("Вычисление ожидаемого результата")
    def calculate(self):
        """
        Выполняет вычисление на основе введенных данных.
        :raise Exception: если оператор неизвестен
        """
        a = int(self.first_number)
        b = int(self.second_number)
        if self.operator == '+':
            return a + b
        elif self.operator == '-':
            return a - b
        elif self.operator == 'x':
            return a * b
        elif self.operator == '÷':
            return a // b

        raise Exception(f"Unknown operator {self.operator}")
