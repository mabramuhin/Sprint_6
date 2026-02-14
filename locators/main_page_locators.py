from selenium.webdriver.common.by import By

class MainPageLocators:

    question_button = (By.CLASS_NAME, "accordion__button")
    answer_panel = (By.XPATH, "//div[@class='accordion__panel']/p")
    header_order_button = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text() = 'Заказать']")
    roadmap_order_button = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']")
    cookie_button = (By.CLASS_NAME, "App_CookieButton__3cvqF")
