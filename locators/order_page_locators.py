from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Локаторы формы 'Для кого самокат'
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_select = (By.XPATH, "//input[@placeholder='* Станция метро']")
    metro_select_item = (By.CLASS_NAME, "select-search__option")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[contains(text(),'Далее')]")

    # Локаторы формы 'Про аренду'
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    period_dropdown_arrow = (By.CLASS_NAME, "Dropdown-arrow")
    period_option = (By.CLASS_NAME, "Dropdown-option")
    color_checkbox_black = (By.ID, "black")
    color_checkbox_grey = (By.ID, "grey")
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[contains(text(),'Заказать')]")
    accept_order_button = (By.XPATH, "//button[contains(text(),'Да')]")
    success_modal = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    show_status_button = (By.XPATH, "//button[contains(text(),'Посмотреть статус')]")