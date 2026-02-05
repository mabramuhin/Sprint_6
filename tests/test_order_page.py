import allure
import pytest

from utils.enums import OrderEntryPoint
from pages.main_page import MainPage
from pages.order_page import OrderPage
from utils.test_data import HEADER_ORDER_DATA, ROADMAP_ORDER_DATA, OrderData
from utils.constants import MAIN_PAGE_URL, DZEN_URL


class TestOrderPage:

    @allure.title("Заказ самоката")
    @pytest.mark.parametrize(
        "entry_point, order_data",
        [
            pytest.param(OrderEntryPoint.HEADER, HEADER_ORDER_DATA),
            pytest.param(OrderEntryPoint.ROADMAP, ROADMAP_ORDER_DATA)
        ])
    def test_create_order(self, driver, entry_point: OrderEntryPoint, order_data: OrderData):
        main_page = MainPage(driver)
        main_page.click_order_button(entry_point)

        order_page = OrderPage(driver)
        order_page.fill_owner_form(order_data.owner)
        order_page.click_next_button()

        order_page.fill_rent_form(order_data.rent)
        order_page.click_order_button()
        order_page.click_accept_order_button()
        assert order_page.check_success_modal_displayed()

        order_page.click_show_status_button()
        order_page.click_scooter_logo()
        assert driver.current_url == MAIN_PAGE_URL

        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        assert driver.current_url == DZEN_URL