
from selenium import webdriver
from CalcPage import CalcPage
import allure


@allure.title("Проверка калькулятора: 7 + 8 = 15")
@allure.description("""Тест проверяет корректность
                    сложения в медленном калькуляторе.""")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Запуск браузера"):
        driver = webdriver.Chrome()

    calc_page = CalcPage(driver)

    with allure.step("Открытие страницы"):
        calc_page.open()

    with allure.step("Установка задержки 45 секунд"):
        calc_page.set_delay("45")

    with allure.step("Нажатие кнопок 7 + 8 ="):
        calc_page.click_button('7')
        calc_page.click_button('+')
        calc_page.click_button('8')
        calc_page.click_button('=')

    with allure.step("Ожидание завершения вычесления"):
        calc_page.wait_spinner()

    with allure.step("Проверка результатов"):
        allure.attach(calc_page.get_result(), "Фактический результат",
                      allure.attachment_type.TEXT)
        allure.attach(str(calc_page.calculate()), "Ожилаемый результат",
                      allure.attachment_type.TEXT)
        assert calc_page.get_result() == str(calc_page.calculate())

    with allure.step("Закрытие браузера"):
        driver.quit()
