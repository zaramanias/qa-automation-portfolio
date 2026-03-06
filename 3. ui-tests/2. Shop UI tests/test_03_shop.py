
from selenium import webdriver
from ShopPage import ShopPage
from CartPage import CartPage
import allure


@allure.title("Проверка итоговой суммы в корзине")
@allure.description("""Тест авторизуется в saucedemo.com,
                    добавляет 3 товара в корзину,
                    оформляет заказ и проверяет итоговую сумму (Total).""")
@allure.feature("Add items / Checkout")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_total():
    with allure.step("Запуск браузера Файрфокс"):
        driver = webdriver.Firefox()

    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)

    with allure.step("Открытие сайта"):
        shop_page.open()

    with allure.step("Авторизация пользователя"):
        shop_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_to_cart()

    with allure.step("Переход в корзину"):
        cart_page.go_to_cart()

    with allure.step("Нажатие кнопки Checkout"):
        cart_page.checkout()

    with allure.step("Заполнение данных покупателя"):
        cart_page.fill_checkout_info("Иван", "Петров", "123456")

    with allure.step("Получение итоговой суммы"):
        value = cart_page.get_result()
        allure.attach(value, name="Полученное значение Total",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Закрытие браузера"):
        driver.quit()

    with allure.step("Проверка итоговой суммы"):
        expected = "Total: $58.29"

        allure.attach(value, name="Фактическая сумма",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(expected, name="Ожидаемая сумма",
                      attachment_type=allure.attachment_type.TEXT)

        assert value == expected
