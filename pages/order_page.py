import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from utils.enums import ScooterColor
from utils.test_data import OwnerData, RentData


class OrderPage(BasePage, OrderPageLocators):

    @allure.step("Заполнить поля формы 'Для кого самокат'")
    def fill_owner_form(self, owner_data: OwnerData):
        self.fill_input(self.name_input, owner_data.name)
        self.fill_input(self.surname_input, owner_data.surname)
        self.fill_input(self.address_input, owner_data.address)
        self.choose_from_dropdown(self.metro_select, self.metro_select_item, owner_data.metro_index)
        self.fill_input(self.phone_input, owner_data.phone)

    @allure.step("Нажать кнопку 'Далее' на форме 'Для кого самокат'")
    def click_next_button(self):
        self.click_after_wait(self.next_button)

    @allure.step("Заполнить поля формы 'Про аренду'")
    def fill_rent_form(self, rent_data: RentData):
        self.fill_input(self.date_input, rent_data.delivery_date)
        self.choose_from_dropdown(self.period_dropdown_arrow, self.period_option, rent_data.period_index)
        self.choose_color(rent_data.scooter_color)
        self.fill_input(self.comment_input, rent_data.comment)

    def choose_color(self, color: ScooterColor):
        with allure.step(f"Выбрать цвет самоката: {color.value}"):
            locator = getattr(self, color.locator_name)
            self.click_after_wait(locator)

    @allure.step("Нажать кнопку 'Заказать' на форме 'Про аренду'")
    def click_order_button(self):
        self.click_after_wait(self.order_button)

    @allure.step("Нажать кнопку 'Да' на форме 'Хотите оформить заказ?'")
    def click_accept_order_button(self):
        self.click_after_wait(self.accept_order_button)

    @allure.step("Проверить отображение формы 'Заказ оформлен'")
    def check_success_modal_displayed(self):
        return self.wait_for_visibility_of_element_located(self.success_modal)

    @allure.step("Нажать кнопку 'Посмотреть статус' на форме 'Заказ оформлен'")
    def click_show_status_button(self):
        self.click_after_wait(self.show_status_button)
